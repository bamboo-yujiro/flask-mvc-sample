from myapp.models.common import *

class Tag(ModelBase):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name):
        self.name = name

    __repr__ = AutoFieldsRepr()
