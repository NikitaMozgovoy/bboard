#!/bin/bash
source /home/www/bboard/env/bin/activate
exec gunicorn -c "/home/www/bboard/samplesite/gunicorn_config.py" samplesite.wsgi

