# Training Blog
Powered by Django & Python

## General idea

This is an Open Blog for everyone. Communication with other using "POST".<br />
Login with your SuperUser.<br />
Go to * [Live](http://b5277.k.dedikuoti.lt:9999/) to see the result and write comments.

## Usefull Commands

* Install virtual environment<br />
`$ pip install pipenv`

* Run virtual environment<br />
`$ pipenv shell`

* Install pipfile, pipfile.lock, requirements.txt at once<br />
`$ pipenv install`

* Check if all requirements are installed<br />
`$ pip list`

![Dependencies](img/pip_list.jpg?raw=true "Pip list")

* To start project you must make migrations<br />
`$ python (or python3) manage.py makemigrations`<br />
`$ python (or python3) manage.py migrate (will migrate all at once)`

* Create SuperUser (admin)<br />
`$ python manage.py createsuperuser`

* Run docker locally<br />
`$ docker-compose up -d`

* List running docker containers
`$ sudo docker ps`

![Alt text](Container.png?raw=true "Container List")

* Run server<br />
`$ python manage.py runserver`

## Install Docker

Before running the server, install docker.

Latest version(not necessary):
* [installing docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
* [installing docker compose](https://docs.docker.com/compose/install/)

Older version apt-get:
* [installing docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
* `$ sudo apt-get install docker-compose`

## Links

* [Live](http://b5277.k.dedikuoti.lt:9999/)

