## Postgresql databases backup
[![Build Status](https://travis-ci.org/yalex2011/pg_dump_backup.svg?branch=master)](https://travis-ci.org/yalex2011/pg_dump_backup) [![codecov](https://codecov.io/gh/yalex2011/pg_dump_backup/branch/master/graph/badge.svg)](https://codecov.io/gh/yalex2011/pg_dump_backup) [![HitCount](http://hits.dwyl.io/yalex2011/https://github.com/yalex2011/pg_dump_backup.svg)](http://hits.dwyl.io/yalex2011/https://github.com/yalex2011/pg_dump_backup) [![GitHub stars](https://img.shields.io/github/stars/yalex2011/pg_dump_backup.svg)](https://github.com/yalex2011/pg_dump_backup/stargazers) [![GitHub issues](https://img.shields.io/github/issues/yalex2011/pg_dump_backup.svg)](https://github.com/yalex2011/pg_dump_backup/issues) [![GitHub license](https://img.shields.io/github/license/yalex2011/pg_dump_backup.svg)](https://github.com/yalex2011/pg_dump_backup/blob/master/LICENSE) [![Updates](https://pyup.io/repos/github/yalex2011/pg_dump_backup/shield.svg)](https://pyup.io/repos/github/yalex2011/pg_dump_backup/) [![Python 3](https://pyup.io/repos/github/yalex2011/pg_dump_backup/python-3-shield.svg)](https://pyup.io/repos/github/yalex2011/pg_dump_backup/)

### Install
```
git clone https://github.com/yalex2011/pg_dump_backup.git
cd pg_dump_backup
pip install -r requirements.txt
```

### Configure app
For the program to work, you need to edit the ini file.
```
nano database.ini
```
Description of the structure of ini file

```markdown
[db1]
host=localhost
database=postgres
user=postgres
password=postgres

[listdb]
db=postgres
path='/tmp/'
```

### Configure cron jobs

In order to set up cron jobs, you need to modify the /etc/crontab file. Please note that this file can only be modified by the root user.
You can edit the crontab file with your favorite text editor, for example
```
nano /etc/crontab
```

add this line
```
0 23 * * * cd /opt/pg_dump_backup && /usr/bin/python /opt/pg_dump_backup/backup.py
```

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
