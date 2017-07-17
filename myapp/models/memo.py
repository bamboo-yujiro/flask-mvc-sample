from myapp.models.common import *

tmp_memo_tags = db.Table('memo_tags', ModelBase.metadata,
    db.Column('memo_id', db.Integer),
    db.Column('tag_id', db.Integer)
)

class Memo(ModelBase):
    __tablename__ = 'memos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    # relationship
    memo_tags = db.relationship('MemoTag', backref='memo', lazy='dynamic', cascade="all", primaryjoin="Memo.id==MemoTag.memo_id", foreign_keys='MemoTag.memo_id')# one to many

    tags = db.relationship("Tag",
        backref="memos",
        primaryjoin="Memo.id==MemoTag.memo_id",
        secondaryjoin="MemoTag.tag_id==Tag.id",
        secondary=tmp_memo_tags,
        lazy='dynamic'
    )


    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id


    def make_tag_str(self):
        tag_str = ''
        for tag in self.tags.all():
            tag_str += tag.name + ','
        self.tag_str = tag_str[:-1]

    def append_tags(self, tag_str):
        from myapp.models.tag import Tag
        from myapp.models.memo_tag import MemoTag
        tag_ids = []
        for tag_name in tag_str.split(','):
            tag = Tag.query.filter(Tag.name == tag_name).first()
            if tag is None:
                tag = Tag(name=tag_name)
                db.session.add(tag)
                db.session.commit()
            if tag.id not in tag_ids:
                memo_tag = MemoTag(tag_id=tag.id, memo_id=None)
                self.memo_tags.append(memo_tag)
                tag_ids.append(tag.id)

    __repr__ = AutoFieldsRepr()
