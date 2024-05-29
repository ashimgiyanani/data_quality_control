# !/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description="Python code to perform data quality control on wind energy data, especially meteorological data",
    author="Ashim Giyanani",
    license="",
    author_email="ashim.giyanani@iwes.fraunhofer.de",
    url='git@gitlab.cc-asp.fraunhofer.de:iwes_wind/PythonProjectTemplate.git',
    keywords=['python', 'template', 'package', 'project'],
    python_requires='>=3.9',
)
