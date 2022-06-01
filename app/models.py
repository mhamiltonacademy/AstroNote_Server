from . import db


engineer_projects= db.Table('engineer_projects',
    db.Column('engineer_id', db.Integer, db.ForeignKey('engineer.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    deadline = db.Column(db.String(20)) # Todo change to Date
    priority = db.Column(db.Integer)
    progress = db.Column(db.Integer)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    engineer_id = db.Column(db.Integer, db.ForeignKey('engineer.id'))
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



class Engineer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    password = db.Column(db.String(200))
    tasks = db.relationship('Task', backref = 'engineer')
    projects = db.relationship('Project', secondary = engineer_projects, backref = 'engineers')
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    is_complete = db.Column(db.Integer, default=0)
    description = db.Column(db.String(2000))
    tasks = db.relationship('Task', backref = 'project')
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


