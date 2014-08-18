#!/bin/bash

NAME="descartes-bi"
DJANGODIR=/usr/share/descartes-bi
SOCKFILE=/var/tmp/gunicorn.sock
USER=www-data
GROUP=www-data
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=descartes_bi.settings.production
DJANGO_WSGI_MODULE=descartes_bi.wsgi
TIMEOUT=600

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind=unix:$SOCKFILE \
  --timeout=$TIMEOUT

