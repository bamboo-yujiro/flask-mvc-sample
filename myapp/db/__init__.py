from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, get_debug_queries, BaseQuery
import env

app.config['SQLALCHEMY_DATABASE_URI'] = env.database_uri
db = SQLAlchemy(app)

class AutoFieldsRepr(object):
    def __get__(self, instance, cls):
        def __repr__():
            attrs = ((f.name, getattr(instance, f.name))
                     for f in cls.__table__.columns)
            # formatting
            formatted = ', '.join("%s=%r" % x for x in attrs)
            return "<%s %s>" % (cls.__name__, formatted)

        return __repr__

class ModelBase(db.Model):

    __abstract__ = True

    query_class = BaseQuery
