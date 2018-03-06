#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(name='fred-pylogger',
      version='1.13.0',
      description='Library contains wrapper for FRED Logger',
      author='Tomáš Diviš, CZ.NIC',
      author_email='vlastimil.zima@nic.cz',
      url='http://www.nic.cz/',
      license='GNU GPL',
      platforms=['posix'],
      packages=find_packages(),
      install_requires=open('requirements.txt').read().splitlines(),
      extras_require={'quality': ['isort', 'flake8', 'pydocstyle']},
      dependency_links=open('dependency_links.txt').read().splitlines())
