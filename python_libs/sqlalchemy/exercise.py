"""
SQLAlchemy exercises

Assuming this table:
    CREATE TABLE employee (
        emp_id INTEGER PRIMARY KEY,
        emp_name VARCHAR(30)
    );
"""

from sqlalchemy import create_engine

engine = create_engine("sqlite:///:memory:")

# creating a employee table
create_table_stmt = (
    "CREATE TABLE employee (emp_id INTEGER PRIMARY KEY, emp_name VARCHAR(30)"
)
engine.execute(create_table_stmt)

# creating an INSERT statement using engine execute() method
insert_stmt = "INSERT INTO employee (emp_name) VALUES (:emp_name)"
engine.execute(insert_stmt, emp_name="karthick")

# SELECT all rows from employee table
result = engine.execute("SELECT * FROM employee")
result.fetchall()
