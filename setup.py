from setuptools import setup, find_packages

setup(
    name='vietadminunits',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'vietadminunits': ['data/*.pkl', 'data/*.db'],
    },
)