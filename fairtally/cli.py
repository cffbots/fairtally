import io
import json
from pathlib import Path
import click
from howfairis import Checker
from howfairis import Compliance
from howfairis import Repo
from jinja2 import Template
from tqdm import tqdm
from fairtally.get_badge_color import get_badge_color
from fairtally.redirect_stdout_stderr import RedirectStdStreams


@click.command()
@click.argument("urls", nargs=-1)
@click.option("-o", "--output-filename", "output_file", help="Where to write the results of the analysis.",
              default=None, type=click.File("wt"))
def cli(urls=None, output_file=None):

    def write_as_json():
        with output_file:
            json.dump(results, output_file, sort_keys=True)

    def write_as_html():
        parent = Path(__file__).parent
        template_file = parent / "data" / "index.html.template"
        with open(template_file) as f:
            template = Template(f.read())
        s = template.render(results=results)
        with output_file:
            output_file.write(s)

    if urls is None:
        print("No URLs provided, aborting.")
        return

    results = list()

    url_progressbar = tqdm(urls, bar_format="fairtally progress: |{bar}| {n_fmt}/{total_fmt}", ncols=70, position=0)
    current_value = tqdm(total=0, bar_format="{desc}", position=1)
    for url in url_progressbar:
        stderr_buffer = io.StringIO()
        stdout_buffer = io.StringIO()
        with RedirectStdStreams(stdout=stdout_buffer, stderr=stderr_buffer):
            try:
                current_value.set_description_str("currently checking " + url)
                repo = Repo(url)
                checker = Checker(repo, ignore_repo_config=True, is_quiet=True)
                compliance = checker.check_five_recommendations()
            except Exception:
                compliance = Compliance(False, False, False, False, False)
            finally:
                badge = "https://img.shields.io/badge/fair--software.eu-{0}-{1}"\
                        .format(compliance.urlencode(), get_badge_color(compliance))
                d = dict(url=url, badge=badge, repository=compliance.repository, license=compliance.license,
                         registry=compliance.registry, citation=compliance.citation, checklist=compliance.checklist,
                         count=compliance.count(), stdout=stdout_buffer.getvalue(), stderr=stderr_buffer.getvalue())

        current_value.set_description_str()
        results.append(d)

    if output_file is None:
        print(json.dumps(results))

    elif output_file.name.endswith(".json"):
        write_as_json()

    elif output_file.name.endswith(".html"):
        write_as_html()

    else:
        raise Exception("Make sure the output file ends with '.html' or '.json'.")


if __name__ == "__main__":
    cli()
