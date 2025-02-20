from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "SURAJ NAHAK"
SRC_REPO = 'src'
LIST_OF_REQUIREMENT = ['falsk']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'surajnahak2016@gmail.com',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    Python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENT,
)