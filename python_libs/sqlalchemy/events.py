"""
SQLAlchemy events registration
"""

from sqlalchemy.event import listens_for
from sqlalchemy.orm import Session


@listens_for(Session, "before_commit")
def custom_before_commit(session):
    print(session)
    print("Echoed before commit action happens...")
