#!/bin/bash
set -e

echo "Entrypoint for $PROJECT_NAME..."
CELERY_BROKER_URL=$QUEUE_PROTOCOL://$QUEUE_USER:$QUEUE_PASSWORD@$QUEUE_HOST:$QUEUE_PORT/$QUEUE_VHOST

echo "CELERY_BROKER_URL:" $CELERY_BROKER_URL
function wait_for_broker {
  set +e
  for try in {1..60} ;  do
    python -c "from kombu import Connection; x=Connection('$CELERY_BROKER_URL', timeout=1); x.connect()" && break
    echo "Waiting for celery broker to respond..."
    sleep 1
  done
}

wait_for_broker

# Run the script to check if the database is working.
bash $SCRIPTS_PATH/check-db.sh

# Check if 'check-db.sh' script exited successfully.
if [ ! $? -ne 0 ]; then

# Run the appropriate command based on TYPE env variable
if [ "$TYPE" = "worker" ]; then
    celery worker -A lms --loglevel=DEBUG --concurrency=16 -Ofair
elif [ "$TYPE" = "beat" ]; then
    celery beat -A lms --loglevel=DEBUG
elif [ "$TYPE" = "api" ]; then
    # Run database and user creation script
    bash $SCRIPTS_PATH/create-db.sh
    # Run the script to apply Django migrations.
    bash $SCRIPTS_PATH/migrate.sh
    # Run the script to run the backend(Django) container.
    bash $SCRIPTS_PATH/run-server.sh
fi
else

 echo "Connection to database server has failed with status code $?. Exiting."
 exit 1;

fi
