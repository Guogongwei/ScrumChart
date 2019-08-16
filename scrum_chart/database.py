from flask_sqlalchemy import SQLAlchemy
from scrum_chart import app

db = SQLAlchemy(app)

class Scrum(db.Model):
    __tablename__ = 'scrum'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer)
    No = db.Column(db.String(255))
    total_sprint = db.Column(db.Integer)
    start_date = db.Column(db.String(255))
    end_date = db.Column(db.String(255))



class ScrumSprint(db.Model):
    __tablename__ = 'scrum_sprint'
    id = db.Column(db.Integer, primary_key=True)
    scrum_id = db.Column(db.Integer)
    day = db.Column(db.String(255))
    left_sprint = db.Column(db.Integer)

