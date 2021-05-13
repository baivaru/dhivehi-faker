#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='dhivehi_faker',
    version='0.1.0',
    author="Baivaru",
    author_email="admin@baivaru.net",
    description="It's like Faker but Dhivehi",
    long_description=open('README.md').read(),
    packages=find_packages(),
    package_data={'': ['*.json', 'data/*.json']},
    include_package_data=True,
    install_requires=[],
    url='https://github.com/phoenixatom/dhivehi-avatar',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    license="GPLv3",
)