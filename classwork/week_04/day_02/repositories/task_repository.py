from db.run_sql import run_sql

def save(task):
    sql = "INSERT INTO tasks (description, assignee, duration, completed) VALUES (%s, %s, %s, %s)"
    values = [task.description, task.assignee, task.duration, task.completed]
    run_sql(sql, values)