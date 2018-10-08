#!/usr/bin/python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

filename = 'database.ini'

def ConfigDB(section):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def ConfigSectionMap(section):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    dict1 = []
    dict1 = parser.get(section, 'db')

    return dict1

def ConfigSectionGet(section, param):

    parser = ConfigParser()
    parser.read(filename)
    result = []
    result = parser.get(section, param)

    return result

def ReadConfig():
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    result = parser.sections()

    return result