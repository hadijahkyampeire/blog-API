[![Build Status](https://travis-ci.org/hadijahkyampeire/blog-API.svg?branch=master)](https://travis-ci.org/hadijahkyampeire/blog-API)
[![Coverage Status](https://coveralls.io/repos/github/hadijahkyampeire/blog-API/badge.svg?branch=master)](https://coveralls.io/github/hadijahkyampeire/blog-API?branch=master)
# blogsApi
This is a simple API blog

## Workflow
Build the image
```
$ docker-compose build
```
Once the build is done, fire up the container in detached mode
```
$ docker-compose up -d
```
Updating the container:
```
$ docker-compose up -d --build
```
Run migrations and create database
```
$ docker-compose exec api-server python manage.py db init
$ docker-compose exec api-server python manage.py db migrate
$ docker-compose exec api-server python manage.py db upgrade
```
With existing migrations, run migrate and upgrade
```
$ docker-compose exec api-server python manage.py db migrate
$ docker-compose exec api-server python manage.py db upgrade
```
Hop into the postgresql(psql) shell
```
docker-compose exec api-db psql -U postgres
```

## Other Commands
To stop the containers:
```
$ docker-compose stop
```
To bring down the containers:
```
$ docker-compose down
```
Want to force a build?
```
$ docker-compose build --no-cache
```
Remove images:
```
$ docker rmi $(docker images -q)
```
