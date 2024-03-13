from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
)