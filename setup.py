from setuptools import setup, find_packages

setup(
    name='nexa_coding_interpreter',
    version='0.6',
    packages=find_packages(),
    install_requires=[
        "nexa-definitions-and-mappings @ git+https://github.com/timlac/nexa-definitions-and-mappings.git"
    ],
)