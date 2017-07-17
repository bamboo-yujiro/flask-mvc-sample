from myapp.models.common import *

class User(ModelBase):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    __repr__ = AutoFieldsRepr()
