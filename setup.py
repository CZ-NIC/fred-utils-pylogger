#!/usr/bin/python
# -*- coding: utf-8 -*-

from freddist.core import setup

PACKAGE_VERSION = '1.0'
PROJECT_NAME = 'fred-pylogger'
PACKAGE_NAME = 'fred-pylogger'

def main():
    setup(
        # Distribution meta-data
        name = PROJECT_NAME,
        description = 'Library contains wrapper for FRED Logger',
        author = 'Tomáš Diviš, CZ.NIC',
        author_email = 'vlastimil.zima@nic.cz',
        url = 'http://www.nic.cz/',
        version = PACKAGE_VERSION,
        license = 'GNU GPL',
        platforms = ['posix'],
        packages = ['pylogger']
    )

if __name__ == '__main__':
    main()