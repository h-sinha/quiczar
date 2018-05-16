# Quiczar

A Quiz Portal having Multiple Choice Questions on various topics.

### Prerequisites

-Django 1.11.13 or above.
-Python 2.7 and Python 3 (3.2, 3.4, 3.5, 3.6)

Django installation on Ubuntu:
```
sudo apt-get update
sudo apt-get install python-django
```
### Directory layout

Quiczar's directory structure looks as follows::

    quiczar/
    ├── manage.py
    ├── quizapp
    └── quizzer
        ├── static
        ├── templatetags
        ├── migrations
        └── templates

### Installation and Running

```
git clone https://github.com/h-sinha/quiczar.git
cd quiczar
python3 manage.py runserver
```
Open localhost:8000 in your web-browser.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Sqlite3](https://www.sqlite.org/docs.html) - Database

## Authors

* **Harsh** - *Initial work* - [h-sinha](https://github.com/h-sinha)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
