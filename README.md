personal-site
=============

Personal site written in Python and Django.

## Installation

Python requirements:

``` shell
pip install -r pip-requirements.txt
```

Dropping and creating the PostgreSQL DB:
``` psql
DROP database <DATABASENAME>;

CREATE database <DATABASENAME>;
```

## Development

To create the DB tables:
``` shell
python manage.py migrate
```

To run the development server:
``` shell
python manage.py runserver
```

## Translations

From the project root:
```
django-admin.py makemessages -a
django-admin.py compilemessages
```

On Mac, we need gettext installed and linked:
```
brew install gettext
brew link gettext
```




