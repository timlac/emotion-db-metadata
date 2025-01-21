from setuptools import setup, find_packages

setup(
    name='nexa_sentimotion_filename_parser',
    version='0.8',
    packages=find_packages(),
    install_requires=[
        "nexa-definitions-and-mappings @ git+https://github.com/timlac/nexa-definitions-and-mappings.git"
    ],
)