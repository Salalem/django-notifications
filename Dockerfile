#
# Notifications API Docker Image
#
# Repository: https://github.com/Salalem/django-notifications
# Maintainers:
#   - Firas Kafri <firas@salalem.com>

# Use 'python:3' as a base image.
FROM python:3.6.5-jessie

# Define environment variables.
ENV PROJECT_NAME "django-notifications-api"
ENV WORKSPACE_PATH "/workspace"
ENV PROJECT_PATH $WORKSPACE_PATH/$PROJECT_NAME
ENV SCRIPTS_PATH $PROJECT_PATH/Dockerfiles/scripts
ENV REQ_TMP_PATH /tmp/requirements

# Force stdin, stdout and stderr to be unbuffered.
ENV PYTHONUNBUFFERED 1

# Install required packages using APT.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libmysqlclient-dev \
    mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy 'requirements.txt' to $REQ_TMP_PATH and install Python packages.
WORKDIR $REQ_TMP_PATH
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy all files in build context, and Python packages to $PROJECT_PATH.
WORKDIR $PROJECT_PATH
RUN cp -a "$REQ_TMP_PATH" .
COPY . .

# Grant 'R-X' permissions to the user for all scripts in $SCRIPTS_PATH.
RUN chmod -R u+rx $SCRIPTS_PATH/*

# Define ENTRYPOINT array with arguments for 'entrpoint.sh'.
ENTRYPOINT ["/bin/bash","Dockerfiles/scripts/entrypoint.sh"]
