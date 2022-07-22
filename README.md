# notes-app

## Frontend App
```bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev

# build for production and launch server
$ yarn build
$ yarn start
```

## Backend App

```bash
# first you need to access to the api folder
$ cd api/

# install dependencies
$ pip install django djangorestframework django-cors-headers

# If you're using a linux distro you might need to change python to python3

# Create the migrations and migrate
$ python manage.py makemigrations
$ python manage.py migrate

# Run the local server
$ python manage.py runserver
```