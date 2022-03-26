"""A setup.py file for setting up and installing this package with pip."""

from setuptools import setup, find_packages


_VERSION = '0.1'

with open("README.md", "r") as _f:
    _README_MD = _f.read()

with open("requirements.txt", "r") as _f:
    _REQUIREMENTS_TXT = _f.read().splitlines()

setup(
    name='project', # TODO: rename.
    version=_VERSION,
    description='An empty Python project.',
    long_description=_README_MD,
    classifiers=[
        # TODO: typing.
        "Typing :: Typed"
    ],
    url="https://github.com/CBreinholt/python-project",  # TODO: project url.
    download_url="", # TODO: download url.
    author="Chris Breinholt",
    author_email="chris.breinholt@gmail.com",
    packages=find_packages(include=['project*']),  # TODO: rename.
    test_suite="tests",  # TODO: tests setup.
    setup_requires=[], # TODO: setup requirements.
    tests_require=[],  # TODO: test requirements.
    install_requires=_REQUIREMENTS_TXT,
    include_package_data=True,
    license='TODO',  # TODO: set license string.
    keywords='empty project TODO keywords'
)