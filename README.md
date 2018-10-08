## Postgresql databases backup
[![Build Status](https://travis-ci.org/yalex2011/pg_dump_backup.svg?branch=master)](https://travis-ci.org/yalex2011/pg_dump_backup) [![codecov](https://codecov.io/gh/yalex2011/pg_dump_backup/branch/master/graph/badge.svg)](https://codecov.io/gh/yalex2011/pg_dump_backup) [![HitCount](http://hits.dwyl.io/yalex2011/https://github.com/yalex2011/pg_dump_backup.svg)](http://hits.dwyl.io/yalex2011/https://github.com/yalex2011/pg_dump_backup) [![GitHub stars](https://img.shields.io/github/stars/yalex2011/pg_dump_backup.svg)](https://github.com/yalex2011/pg_dump_backup/stargazers) [![GitHub issues](https://img.shields.io/github/issues/yalex2011/pg_dump_backup.svg)](https://github.com/yalex2011/pg_dump_backup/issues) [![GitHub license](https://img.shields.io/github/license/yalex2011/pg_dump_backup.svg)](https://github.com/yalex2011/pg_dump_backup/blob/master/LICENSE) [![Updates](https://pyup.io/repos/github/yalex2011/pg_dump_backup/shield.svg)](https://pyup.io/repos/github/yalex2011/pg_dump_backup/) [![Python 3](https://pyup.io/repos/github/yalex2011/pg_dump_backup/python-3-shield.svg)](https://pyup.io/repos/github/yalex2011/pg_dump_backup/)


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



You can use the [editor on GitHub](https://github.com/yalex2011/pg_dump_backup/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/yalex2011/pg_dump_backup/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
