"""
SQLAlchemy
"""

import time
from random import randint, choice
from typing import List

from sqlalchemy.orm import Session

from models import Scheduler, TriggerType, Tracker
from utils import get_db_env, get_mysql_engine

engine = get_mysql_engine(*get_db_env())

jobs = ["helloworld", "welcome", "thankyou", "goodbye", "please"]


def execute(source_function):
    def wrapper(*args, **kwargs):
        # TODO: To add try catch block
        with Session(engine) as session:
            session.flush()
            res = source_function(*args, **kwargs)

            if isinstance(res, list):
                session.add_all(res)

            if isinstance(res, (Scheduler, Tracker)):
                session.add(res)

            session.commit()

    return wrapper


# using ORMs Session object
@execute
def scheduler_insert(
    job_name: str, trigger_type: TriggerType, trigger_args: dict
) -> Scheduler:
    return Scheduler(
        job_name=job_name,
        trigger_type=trigger_type,
        trigger_args=trigger_args,
    )


@execute
def scheduler_bulk_insert() -> List[Scheduler]:
    return [
        Scheduler(
            job_name=f"print_{choice(jobs)}",
            trigger_type=TriggerType.INTERVAL.value,
            trigger_args={"seconds": 5},
        )
        for _ in range(1, 7)
    ]


@execute
def track_insert(scheduler_id: int) -> Tracker:
    return Tracker(scheduler_id=scheduler_id)


@execute
def track_bulk_insert() -> List[Tracker]:
    return [
        Tracker(scheduler_id=randint(1, 10))
        for _ in range(1, 6)
        if time.sleep(1) is None
    ]


def main():
    # scheduler_insert("print_welcome", TriggerType.INTERVAL.value, {"seconds": 5})
    # scheduler_bulk_insert()

    # track_bulk_insert()
    track_insert(18)


if __name__ == "__main__":
    main()
