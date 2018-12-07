#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2018  CZ.NIC, z. s. p. o.
#
# This file is part of FRED.
#
# FRED is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FRED is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FRED.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import find_packages, setup

setup(name='fred-pylogger',
      version='1.15.0',
      description='Library contains wrapper for FRED Logger',
      author='Tomáš Diviš, CZ.NIC',
      author_email='vlastimil.zima@nic.cz',
      url='http://www.nic.cz/',
      license='GPLv3+',
      platforms=['posix'],
      packages=find_packages(),
      install_requires=open('requirements.txt').read().splitlines(),
      extras_require={'quality': ['isort', 'flake8', 'pydocstyle']},
      dependency_links=open('dependency_links.txt').read().splitlines())
