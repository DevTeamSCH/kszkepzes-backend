# KSZKépzés Honlap

[![Build Status](https://travis-ci.org/DevTeamSCH/kszkepzes.svg?branch=master)](https://travis-ci.org/DevTeamSCH/kszkepzes)

[![CircleCI](https://circleci.com/gh/DevTeamSCH/kszkepzes/tree/master.svg?style=svg)](https://circleci.com/gh/DevTeamSCH/kszkepzes/tree/master)

## Követelmények

1. python3.5
2. pip

## Fejlesztés

1. python3 -m venv venv
2. source venv/bin/activate
3. cp environment.sh.example environment.sh
4. Ki kell tölteni a környezeti változókat.  
Az authsch-s adatokat az https://auth.sch.bme.hu/ fejlesztői konzol menüpontja alatt lehet legenerálni új kliens hozzáadásával.
Atirányítási cím: `http://127.0.0.1:3000/api/v1/complete/authsch`
```shell script
   export SECRET_KEY=<Ide bármi kerülhet>
   export AUTHSCH_KEY=<authsch-s Kliens azonosító>
   export AUTHSCH_SECRET=<authsch-s Kliens kulcs>
   export MEDIA_ROOT=static/
  ```
5. source environment.sh
6. pip install -r requirements/development.txt
7. python3 src/manage.py runserver

## Formális Követelmények
1. flake8-nak feleljen meg
2. 125 karakternél ne legyen hosszabb sor

> TODO: Böviteni a követelményeket

> TODO: Windows-os leírás
