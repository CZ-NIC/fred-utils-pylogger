#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(name='fred-pylogger',
      version='1.12.0',
      description='Library contains wrapper for FRED Logger',
      author='Tomáš Diviš, CZ.NIC',
      author_email='vlastimil.zima@nic.cz',
      url='http://www.nic.cz/',
      license='GNU GPL',
      platforms=['posix'],
      packages=find_packages(),
      install_requires=['fred-pyfco'],
      dependency_links=['git+ssh://git@gitlab.office.nic.cz/fred/utils/pyfco.git@master#egg=fred-pyfco-0'])
