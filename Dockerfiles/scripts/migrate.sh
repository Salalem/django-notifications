#!/bin/bash

echo "Running database migrations for $PROJECT_NAME..."

# Echo the current $BUILD_PROFILE
echo "Current Build Profile: $BUILD_PROFILE"

if [ "$BUILD_PROFILE" = "development" ]; then

echo "Migrating the database..."
python $PROJECT_PATH/manage.py migrate

elif [ "$BUILD_PROFILE" = "staging" ]; then

echo "Migrating the database..."
python $PROJECT_PATH/manage.py migrate --settings=salalem_notifications.settings.production

elif [ "$BUILD_PROFILE" = "production" ]; then

echo "Migrating the database..."
python $PROJECT_PATH/manage.py migrate --settings=salalem_notifications.settings.production

echo "No specific migrations/fixtures for production"
fi
