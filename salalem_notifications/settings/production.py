from .base import *

# Databases environment variables
DB_NAME = os.environ.get("DB_NAME", "notifications")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "QWEqwe!1")
DB_HOSTNAME = os.environ.get("DB_HOSTNAME", "localhost")
DB_PORT = os.environ.get("DB_PORT", "3306")

DATABASES = {
    "default": {
        "ENGINE": "mysql_server_has_gone_away",
        "CONN_MAX_AGE": 3600,
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOSTNAME,
        "PORT": DB_PORT,
    }
}
