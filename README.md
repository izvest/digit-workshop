# Digit Project

Hello! I am the Digit & Anders workshop project.


## Development


### Creating and updating requirements

* Run `prequ update`


### Installing requirements

* Run `pip install -r requirements.txt`
* Run `pip install -r requirements-dev.txt`


### Database

Docker environment has working database set up out of the box. If for
any reason there's a need to recreate it, here's how to do it:

    docker exec -i digit_mysql mysql -uroot -pdigit_project -e "CREATE USER 'digit_project'@'localhost' IDENTIFIED BY 'digit_project';"
    docker exec -i digit_mysql mysql -uroot -pdigit_project -e "CREATE DATABASE digit_project;"
    docker exec -i digit_mysql mysql -uroot -pdigit_project -e "GRANT ALL PRIVILEGES ON digit_project.* TO 'digit_project'@'localhost';"


### Daily running

* Set the `DEBUG` environment variable to `1`.
* Run `python manage.py migrate`
* Run `python manage.py runserver 0:8000`


## Running tests

* Set the `DEBUG` environment variable to `1`.
* Run `pytest`.
