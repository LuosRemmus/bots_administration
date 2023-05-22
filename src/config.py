import logging
from pydantic import BaseSettings, BaseModel


class DBConfig(BaseModel):
    user: str = "postgres"
    password: str = "postgres"
    host: str = "localhost"
    port: int = 5432
    database: str = "postgres"

    @property
    def dsn(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class Config(BaseSettings):
    database: DBConfig = DBConfig()
    log_level: int = logging.DEBUG
    
    class Config:
        env_nested_delimiter='__'
        env_file=".env"


config = Config()
