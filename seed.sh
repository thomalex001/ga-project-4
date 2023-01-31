#!/bin/bash

echo "dropping database custom-bikes"
dropdb custom-bikes

echo "creating database custom-bikes"
createdb custom-bikes

python3 manage.py makemigrations

python3 manage.py migrate

echo "inserting users"
python3 manage.py loaddata jwt_auth/seeds.json

echo "inserting products"
python3 manage.py loaddata products/seeds.json

echo "inserting type"
python3 manage.py loaddata type/seeds.json
