from app import db, app
from app import Task

with app.app_context():
    db.create_all()

    if Task.query.count() == 0:
        tasks = [
            Task(name='Backup the database', description='Make sure to backup the database with all the tables.'),
            Task(name='Setup 2FA', description='Setup the two factor authentication to secure your account.'),
            Task(name='Malware scan', description='Perform a malware scan.'),
        ]

        for task in tasks:
            db.session.add(task)

        db.session.commit()
