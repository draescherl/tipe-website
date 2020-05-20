# Mini-loon project

A presentation tool using the Django framework.

## Getting Started
---

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### General prerequisites

Add-ons you will need to run our project.

From the folder where you want to install our project, create a virtual environment to run Python :
```
virtualenv env -p python3
```

Activate the environment :
```
. env/bin/activate
```

Install Django in your virtualenv :
```
pip install django
```
Our code was written with version 3.0.5.
You can check your version by running :
```
python -m django --version
```
Any later version should work correctly.


### Installing PostgreSQL

We used PostgreSQL as our database software. If you're already comfortable using something else, feel free to skip this part but you'll have to change a few lines of code in `settings.py` (look for a line starting with DATABASES = {...}).

Installing psycopg2 :
```
pip install psycopg2-binary
```

Installing PostgreSQL :
```
sudo apt-get install postgresql
```

Starting PostgreSQL :
```
sudo service postgresql start
```

### Creating a database

## Installing our project
---

The final piece of software you will need to install is the django debug toolbar :
```
pip install django-debug-toolbar
```

You can now go ahead and clone our project into your current directory.

## Built With
---

* [Django](https://www.djangoproject.com/) - The web framework used
* [Shower](https://github.com/shower/shower) - The template used
 

## Authors
---

* **Hugo Cambra** - cambralefe@eisti.eu
* **Lucas Draescher** - draescherl@eisti.eu
* **Thomas Olivier** - oliviertho@eisti.eu
* **Antonin Soulier** - soulierant@eisti.eu

## License
---

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
