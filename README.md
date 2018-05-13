## renefernandez.com personal website

[![Build Status](https://travis-ci.org/renefs/personal-site.svg?branch=master)](https://travis-ci.org/renefs/personal-site)

[![Maintainability](https://api.codeclimate.com/v1/badges/656018ee193b8014f31a/maintainability)](https://codeclimate.com/github/renefs/personal-site/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/656018ee193b8014f31a/test_coverage)](https://codeclimate.com/github/renefs/personal-site/test_coverage)

Requirements:

- Docker
- Docker Compose
- Python 3.5


### OS X Instructions

1. Copy `web/config.sample.py` to `web/config.py`
1. Build image - `docker-compose build`
1. Start service - `docker-compose up`
1. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate`
1. Access - `http://127.0.0.1:8000`

```
python manage.py makemessages -l <LANGUAGE_CODE> (es|en)
python manage.py makemessages -a
python manage.py compilemessages
```