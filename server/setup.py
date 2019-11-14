from __future__ import absolute_import
from __future__ import print_function

import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def readme() -> str:
    """Utility function to read the README file.

    Used for the long_description.  It's nice, because now 1) we have a top
    level README file and 2) it's easier to type in the README file than to put
    a raw string in below.
    :return: content of README.md
    """
    return open(join(dirname(__file__), "README.md")).read()


def dev_requirements():
    """Parse dev-requirements.txt to array of packages to have installed.
    :return: list of dev requirements
    """
    with open("dev-requirements.txt") as f:
        return f.read().splitlines()


def version() -> str:
    """Utility function to read version for project.
    :return: version for package
    """
    with open("src/__init__.py", "rt", encoding="utf8") as f:
        return re.search(r'__version__ = "(.*?)"', f.read()).group(1)


setup(
    name="fastapi-vue-crud-server",
    version=version(),
    author="Fanilo Andrianasolo",
    author_email="andfanilo@gmail.com",
    description="FastAPI server.",
    long_description=readme(),
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    install_requires=["fastapi", "uvicorn"],
    extras_require={"dev": dev_requirements()}
)
