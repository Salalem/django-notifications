#!/bin/bash
set -e

echo "Running database check script..."

TRIALS=10
COUNTER=1

# Wait until the db container is working before attempting apply django migrations.
while ! mysqladmin ping -h"$DB_HOSTNAME" -P $DB_PORT --user=$DB_USER --password=$DB_PASSWORD; do
    echo "#$COUNTER: Still waiting for MySQL server on host $DB_HOSTNAME:$DB_PORT"
    sleep 5

    if [[ $COUNTER = $TRIALS ]]; then
        echo "Failed to connect to MySQL server on $DB_HOSTNAME:$DB_PORT after $COUNTER trails. Exiting."
        exit 1;
    else
        COUNTER=$(($COUNTER +1))
    fi
done

echo "$DB_HOSTNAME:$DB_PORT is up and running."
