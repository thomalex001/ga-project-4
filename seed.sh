#!/bin/bash

echo "dropping database custom-bikes"
dropdb custom-bikes

echo "creating database custom-bikes"
createdb custom-bikes

python manage.py makemigrations

python manage.py migrate

echo "inserting users"
python manage.py loaddata jwt_auth/seeds.json

echo "inserting products"
python manage.py loaddata products/seeds.json

echo "inserting cart"
python manage.py loaddata cart/seeds.json

echo "inserting type"
python manage.py loaddata type/seeds.json

