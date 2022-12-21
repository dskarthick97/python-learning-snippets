"""
SQLAlchemy Trigger model
"""

import enum

from sqlalchemy import JSON, Column, Enum, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

from utils import get_mysql_engine, get_db_env

Base = declarative_base()


class TriggerType(enum.Enum):
    DATE = "date"
    INTERVAL = "interval"
    CRON = "cron"


class Scheduler(Base):
    __tablename__ = "scheduler"

    job_id = Column(
        "id",
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
    )
    job_name = Column(String(255), nullable=False)
    trigger_type = Column(
        Enum(*[trigger_type.value for trigger_type in TriggerType]),
        nullable=False,
    )
    trigger_args = Column(JSON)
    create_ts = Column(DateTime, nullable=False, default=func.now())

    def __repr__(self) -> str:
        return (
            f"Scheduler(job_id={self.job_id}, job_name={self.job_name}, "
            f"trigger_type={self.trigger_type}, trigger_args={self.trigger_args})"
        )


class Tracker(Base):
    __tablename__ = "tracker"

    track_id = Column(
        "id", Integer, nullable=False, primary_key=True, autoincrement=True
    )
    scheduler_id = Column(Integer, nullable=False)
    create_ts = Column(DateTime, nullable=False, default=func.now())

    def __repr__(self):
        return f"Tracker(track_id={self.track_id}, scheduler_id={self.scheduler_id})"


engine = get_mysql_engine(*get_db_env())
Base.metadata.create_all(engine)
