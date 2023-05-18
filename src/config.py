import logging
import os
from dotenv import load_dotenv
from pydantic import BaseSettings, BaseModel

"""load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

PGADMIN_PW = os.environ.get("PGADMIN_PW")
PGADMIN_MAIL = os.environ.get("PGADMIN_MAIL")"""



class DBConfig(BaseModel):
    user: str = "postgres"
    password: str = "postgres"
    host: str = "localhost"
    port: int = 5432
    database: str = "postgres"

    @property
    def dsn(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

# Тут советую настоятельно использовать pydantic
class Config(BaseSettings):
    database: DBConfig = DBConfig()
    log_level: int = logging.DEBUG
    
    class Config:
        env_nested_delimiter='__'
        env_file=".env"


config = Config()
