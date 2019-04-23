#!/bin/bash

echo "$PROJECT_NAME API is running..."

echo "Current Build Profile: $BUILD_PROFILE"
echo "ALLOWED_HOSTS: $ALLOWED_HOSTS"
cd $PROJECT_PATH

if [ "$BUILD_PROFILE" = "development" ]; then

# Run the Django server with development settings
python ./manage.py runserver 0.0.0.0:8000

elif [ "$BUILD_PROFILE" = "staging" ]; then
# Start Gunicorn processes
echo "Starting Gunicorn with $GUNICORN_WORKERS workers..."

exec gunicorn wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1 \
    --log-level=debug

elif [ "$BUILD_PROFILE" = "production" ]; then
# Start Gunicorn processes
echo "Starting Gunicorn with $GUNICORN_WORKERS workers..."

exec gunicorn wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers $GUNICORN_WORKERS \
    --log-level=debug
fi
