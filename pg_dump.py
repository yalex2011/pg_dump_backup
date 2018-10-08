#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import datetime

def RunPG_dump (host_name, user_name, password, database_name, path_backup):
      dt = datetime.datetime.now()
      date = dt.strftime("%Y-%m-%d-%H.%M.%S")

      file_name = date + '-' + database_name + '.tar.gz'

      cmd = 'cd ' + path_backup + '&& export PGPASSWORD={3} && '+'pg_dump -h {0} -U {1} --clean --create --format=t {2} | gzip > {4}'\
            .format(host_name, user_name, database_name, password, file_name)

      popen = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

      popen.stdout.close()
      popen.wait()
