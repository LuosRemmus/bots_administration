import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

PGADMIN_PW = os.environ.get("PGADMIN_PW")
PGADMIN_MAIL = os.environ.get("PGADMIN_MAIL")
