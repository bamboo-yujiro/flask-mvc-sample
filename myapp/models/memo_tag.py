from myapp.models.common import *

class MemoTag(ModelBase):
    __tablename__ = 'memo_tags'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer)
    memo_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, tag_id, memo_id):
        self.tag_id = tag_id
        self.memo_id = memo_id

    __repr__ = AutoFieldsRepr()
