from flask_sqlalchemy import SQLAlchemy
from scrum_chart import app

db = SQLAlchemy(app)

class Scrum(db.Model):
    __tablename__ = 'scrum'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(255))
    No = db.Column(db.String(255))
    total_sprint = db.Column(db.Integer)
    start_date = db.Column(db.String(255))
    end_date = db.Column(db.String(255))