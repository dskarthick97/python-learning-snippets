"""
Execution handler

- https://docs.sqlalchemy.org/en/14/tutorial/index.html#unified-tutorial
- https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
- https://www.youtube.com/watch?v=woKYyhLCcnU&t=3s&ab_channel=NextDayVideo
- https://www.youtube.com/watch?v=sO7FFPNvX2s

Assumptions:
    - both the tables are in same db
    - `id` columns of both the Scheduler and Tracker tables are ordered (auto incremented)
    - there is at-least one record in tracker table

    - creating a new record instead of updating in `tracker` table
    - selecting max scheduler id instead of max id in tracker table

Scenarios to handle:
    - Handle the inaugural select request of tracker table
    - What if there is no records inserted into scheduler table in the scheduled
        interval -- List out of index error
    - buffer for millions of record
    - handle the deleted row data -- Error queue
"""

from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import Tracker, Scheduler
from utils import get_db_env, get_mysql_engine


def process(sqlalchemy_engine):
    with Session(sqlalchemy_engine) as session:
        with session.begin():
            # selecting last row_id from tracker table
            tracker_select_stmt = select(func.max(Tracker.scheduler_id))
            sched_id = session.scalar(tracker_select_stmt)

            # selecting all records after a specific record
            scheduler_select_stmt = select(Scheduler).where(
                Scheduler.job_id > sched_id)
            records = session.scalars(scheduler_select_stmt).all()
            print(records)

            # updating the tracker table with last record id
            last_record_id = records[-1].job_id
            session.add(Tracker(scheduler_id=last_record_id))


def main():
    engine = get_mysql_engine(*get_db_env())

    scheduler = BackgroundScheduler()
    scheduler.add_job(process, "interval", seconds=30, args=[engine])
    scheduler.start()

    try:
        while True:
            sleep(28)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


if __name__ == "__main__":
    # engine = get_mysql_engine(*get_db_env())
    # process(engine)

    main()
