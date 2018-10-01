# Digit Project

Hello! I am the Digit & Anders workshop project.
My developers are lazy and haven't written a good README.

## Development

### Creating and updating requirements

* Run `prequ update`

### Installing requirements

* Run `pip install -r requirements.txt`
* Run `pip install -r requirements-dev.txt`

### Database

To setup a database compatible with default database settings:

Create user and database

    sudo -u postgres createuser -P -R -S digit_project  # use password `digit_project`
    sudo -u postgres createdb -O digit_project digit_project

Allow user to create test database

    sudo -u postgres psql -c "ALTER USER digit_project CREATEDB;"

### Daily running

* Set the `DEBUG` environment variable to `1`.
* Run `python manage.py migrate`
* Run `npm run build`
* Run `python manage.py runserver 0:8000`

## Running tests

* Set the `DEBUG` environment variable to `1`.
* Run `py.test`.

