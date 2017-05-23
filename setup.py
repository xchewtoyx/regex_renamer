#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='regexrename',
    version='0.0.1',
    description='Regex Rename',
    author='Russell Heilling',
    author_email='russell@heilling.net',
    packages=find_packages(),
    install_requires=[
        'cement>=2.6.0,<2.11',
    ],
    entry_points={
        'console_scripts': [
            'rrn=regex_rename.cli:main',
        ],
    },
)
