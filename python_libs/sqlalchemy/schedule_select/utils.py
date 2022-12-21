"""
Utility functions
"""

from os import getenv
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.future.engine import Engine

load_dotenv()


def get_db_env() -> tuple:
    return (
        getenv("DB_USERNAME"),
        getenv("DB_PASSWORD"),
        getenv("DB_HOST"),
        getenv("DB_NAME"),
    )


def get_mysql_engine(username: str, password: str, host: str, database: str) -> Engine:
    quoted_password = quote_plus(password)

    return create_engine(
        f"mysql+pymysql://{username}:{quoted_password}@{host}/{database}",
        echo=False,
        future=True,
    )
