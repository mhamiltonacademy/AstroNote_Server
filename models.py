from app import db


engineer_projects= db.Table('engineer_projects',
    db.Column('engineer_id', db.Integer, db.ForeignKey('engineer.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    deadline = db.Column(db.Date)
    priority = db.Column(db.Integer)
    progress = db.Column(db.Integer)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    engineer_id = db.Column(db.Integer, db.ForeignKey('engineer.id'))



class Engineer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    password = db.Column(db.String(200))
    tasks = db.relationship('Task', backref = 'engineer')
    projects = db.relationship('Project', secondary = engineer_projects, backref = 'engineers')



class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    is_complete = db.Column(db.Boolean)
    tasks = db.relationship('Task', backref = 'project')




db.create_all()