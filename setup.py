#!/usr/bin/env python
import os
from fairtally.__version__ import __version__
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# # To update the package version number, edit CITATION.cff
# with open("CITATION.cff", "r") as cff:
#     for line in cff:
#         if "version:" in line:
#             version = line.replace("version:", "").strip().strip('"')

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="fairtally",
    entry_points={
        "console_scripts": ["fairtally=fairtally.cli:cli"],
    },
    version=__version__,
    description="Make a report based on howfairis results",
    long_description=readme + "\n\n",
    author="FAIR Software",
    author_email="j.spaaks@esciencecenter.nl",
    url="https://github.com/fair-software/fairtally",
    packages=[
        "fairtally",
    ],
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="fairtally",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    test_suite="tests",
    install_requires=[
        "click == 7.*",
        "howfairis == 0.13.*",
        "requests == 2.*",
        "tqdm == 4.*"
    ],
    setup_requires=[
    ],
    tests_require=[
    ],
    extras_require={
        "dev": [
            "bumpversion",
            "prospector[with_pyroma]",
            "pycodestyle",
            "pytest-cov",
            "pytest-runner",
            "pytest",
            "recommonmark",
            "sphinx_rtd_theme",
            "sphinx-click",
            "sphinx",
            "yapf"
        ],
        "publishing": [
            "twine",
            "wheel"
        ]
    },
    data_files=[("citation/fairtally", ["CITATION.cff"])]
)
