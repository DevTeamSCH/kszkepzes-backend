# KSZKépzés Honlap

[![pipeline status](https://git.sch.bme.hu/kszk/devteam/kszkepzes/badges/master/pipeline.svg)](https://git.sch.bme.hu/kszk/devteam/kszkepzes/commits/master)
[![coverage report](https://git.sch.bme.hu/kszk/devteam/kszkepzes/badges/master/coverage.svg)](https://git.sch.bme.hu/kszk/devteam/kszkepzes/commits/master)

## Követelmények

1. python3.5
2. pip

## Fejlesztés

1. python3 -m venv venv
2. source venv/bin/activate
3. mv environment.sh.example environment.sh
4. Ki kell tölteni a környezeti változókat.
5. source environment.sh
6. pip install -r requirements/development.txt
7. python3 src/manage.py runserver

## Formális Követelmények
1. flake8-nak feleljen meg
2. 125 karakternél ne legyen hosszabb sor

> TODO: Böviteni a követelményeket

> TODO: Windows-os leírás
