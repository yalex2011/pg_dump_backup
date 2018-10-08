#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import config
import pg_dump

def connect(section):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config.ConfigDB(section)

        # connect to the PostgreSQL server
        print ('Connecting to the PostgreSQL database from ', section)
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print ('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def get_databases(section):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config.ConfigDB(section)
        result=[]
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        # execute a statement
        print('Get databases:')
        cur.execute("""SELECT datname FROM pg_database
            WHERE datistemplate = false;""")
        # display the PostgreSQL database server version
        for table in cur.fetchall():
            result.append(table)
            #print(table)

     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return result

if __name__ == '__main__':
    #connect()
    sections = config.ReadConfig()
    listdb = config.ConfigSectionMap('listdb').split(',')
    path_backup = config.ConfigSectionGet('listdb','path')

    for section in sections:

        if section != 'listdb':
            host_name = config.ConfigSectionGet(section, 'host')
            user_name = config.ConfigSectionGet(section, 'user')
            password = config.ConfigSectionGet(section, 'password')

            res = get_databases(section)

            for r in res:
                if r[0] in listdb:
                    print ('Starting backup database:')
                    database_name = r[0]
                    print database_name
                    pg_dump.RunPG_dump(host_name, user_name, password, database_name, path_backup)
                    print ('Backup complite')
