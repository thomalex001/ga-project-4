#!/bin/bash

echo "creating products/seeds.json"
python manage.py dumpdata products --output products/seeds.json --indent=2;

echo "creating type/seeds.json"
python manage.py dumpdata type --output type/seeds.json --indent=2;

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;