# recipe-app-api
Recipe API project.

COMMANDS
docker build .
docker-compose build
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "python manage.py test"

#create the django app via docker
docker-compose run --rm app sh -c "django-admin startproject app ."


# start services
docker-compose up

# run test
docker-compose run --rm app sh -c "python manage.py test"

# rebuild services after adding the postgress
docker-compose build

# build app to check for race condition that Postgres is actually up.
docker-compose run --rm app sh -c "python manage.py startapp core"