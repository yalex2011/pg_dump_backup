#!/usr/bin/python
# -*- coding: utf-8 -*-

# import datetime
# from subprocess import PIPE,Popen
# import shlex
#
# def dump_table(host_name,database_name,user_name,database_password,table_name):
#
#     command = 'pg_dump -h {0} -d {1} -U {2} -p 5432 -t public.{3} -Fc -f /tmp/table.dmp'\
#     .format(host_name,database_name,user_name,table_name)
#
#     p = Popen(command,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
#
#     return p.communicate('{}\n'.format(database_password))

# import datetime
# import gzip
# import subprocess
#
# host_name = '192.168.1.177'
# database_name = 'test_db'
# user_name = 'postgres'
# pg_pass = 'postgres'
#
# cmd = 'export PGPASSWORD={3} && pg_dump -h {0} -d {1} -U {2} -p 5432 -Fc -f /tmp/table.dmp'\
#       .format(host_name,database_name,user_name,pg_pass)
#
# print cmd
#
# with gzip.open('backup.gz', 'wb') as f:
#     popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
#
#     for stdout_line in iter(popen.stdout.readline, ""):
#         f.write(stdout_line.encode('utf-8'))
#
#         popen.stdout.close()
#         popen.wait()

import subprocess
import datetime

def RunPG_dump (host_name,user_name,database_name,path_backup):
      dt = datetime.datetime.now()
      date = dt.strftime("%Y-%m-%d-%H.%M.%S")

      file_name = date + '-' + database_name + '.tar.gz'

      cmd = 'cd ' + path_backup + ' && '+'pg_dump -h {0} -U {1} --clean --create --format=t {2} | gzip > {3}'\
            .format(host_name, user_name, database_name, file_name)

      popen = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

      popen.stdout.close()
      popen.wait()
