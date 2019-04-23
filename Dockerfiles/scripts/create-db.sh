#!/bin/bash
set -e

echo "Running database creation script for $PROJECT_NAME..."

# Echo the current $BUILD_PROFILE
echo "Current Build Profile: $BUILD_PROFILE"

if [ "$BUILD_PROFILE" = "development" ]; then
mysql -h $DB_HOSTNAME --user='root' --password=$DB_PASSWORD < $SCRIPTS_PATH/createdbs.sql

elif [ "$BUILD_PROFILE" = "staging" ]; then
mysql -h $DB_HOSTNAME --user='root' --password=$DB_PASSWORD < $SCRIPTS_PATH/createdbs.sql

elif [ "$BUILD_PROFILE" = "production" ]; then
echo "No database operations for production"
fi
