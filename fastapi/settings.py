import enum
from pathlib import Path
from tempfile import gettempdir
from typing import List, Optional

from pydantic import BaseSettings
from yarl import URL
import os
import dotenv
dotenv.load_dotenv()

TEMP_DIR = Path(gettempdir())

class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO

    # Variables for the database
    db_host: str = "localhost"
    db_port: int = os.environ.get("FASTAPI_DB_PORT")
    db_user: str = os.environ.get("FASTAPI_DB_USER")
    db_pass: str = os.environ.get("FASTAPI_DB_PW")
    db_base: str = "fastapi"
    db_echo: bool = False


    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="mysql+aiomysql",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}",
        )

    class Config:
        env_file = ".env"
        env_prefix = "FASTAPI_"
        env_file_encoding = "utf-8"


settings = Settings()
