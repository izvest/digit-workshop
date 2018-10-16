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

* Run `docker-compose build django` to build development environment docker image
* Run 'docker-compose up` to start the development environment


## Running tests

* Set the `DEBUG` environment variable to `1`.
* Run `pytest`.
