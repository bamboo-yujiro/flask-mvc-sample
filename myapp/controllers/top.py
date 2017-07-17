from myapp.controllers import *
from flask_wtf import Form
from wtforms import validators
from wtforms.fields import TextField, BooleanField
from wtforms.validators import Required
from flask import g
from myapp.valiables.hoge import hoge
from myapp.controllers.general_base import GeneralBaseView


class TopView(GeneralBaseView):

    route_base='/'
    per_page = 5

    def before_request(self, name, **view_args):
        self.auth_redirect = False
        return super().before_request(name, **view_args)

    @route('/')
    def index(self):
        return render_template('top/index.html')
