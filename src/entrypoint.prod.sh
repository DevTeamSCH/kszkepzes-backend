#!/bin/sh

if [ "$DJANGO_SETTINGS_MODULE" = "kszkepzes.settings.production" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"