#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(name='fred-pylogger',
      description='Library contains wrapper for FRED Logger',
      author='Tomáš Diviš, CZ.NIC',
      author_email='vlastimil.zima@nic.cz',
      url='http://www.nic.cz/',
      license='GNU GPL',
      platforms=['posix'],
      packages=find_packages(),
      install_requires=['pyfco'],
      dependency_links=['git+ssh://git@gitlab.office.nic.cz/utils/pyfco.git@master#egg=pyfco-0'])
