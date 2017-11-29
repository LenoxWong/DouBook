#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LenoxWong'


DEFAULT = {
    # what you want to search
    'search': '妖怪',
    # what rate do you want
    'rate': 8.0
}

# The file name you want data stored, there is  妖怪(8.0+).json
# you can chang it to anything you want
# such as myfile.json or myfile.txt
SAVED = '%s(%s+).json' % (DEFAULT['search'], DEFAULT['rate'])
