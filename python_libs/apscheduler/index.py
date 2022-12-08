"""
APScheduler
"""

from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler


def job_one():
    print("Executing job_one...")


sched = BlockingScheduler()
sched.add_job(job_one, "interval", seconds=5)
sched.start()

# while True:
#     sleep(3)
