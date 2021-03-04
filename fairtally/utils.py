import json
from pathlib import Path
from typing import TextIO, List


def merge_urls(urls: List[str], input_file: TextIO):
    all_urls = list(urls)
    if input_file is not None:
        for line in input_file:
            url = line.strip()
            if url:
                all_urls.append(url)
    return all_urls


def write_as_html(results, output_file_html):
    parent = Path(__file__).parent
    template_file = parent / "data" / "index.html.template"
    with open(template_file) as f:
        template_str = f.read()
    report = template_str.replace("{{python inserts the data here}}", json.dumps(results))
    with output_file_html:
        output_file_html.write(report)


def write_as_json(results, output_file_json):
    with output_file_json:
        json.dump(results, output_file_json, sort_keys=True)
