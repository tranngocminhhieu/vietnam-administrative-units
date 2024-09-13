from setuptools import setup, find_packages

setup(
    name='vnau_parser',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'vnau_parser': ['data/*.pkl'],
    },
)