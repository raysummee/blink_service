from app import db


class Settings(db.Model):
    active = db.Column(db.Boolean)