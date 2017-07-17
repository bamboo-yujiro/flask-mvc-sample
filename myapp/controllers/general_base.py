from app import app
from myapp.controllers import *
from flask import Blueprint, render_template, redirect, url_for, request
from flask_wtf import Form
from wtforms import validators
from wtforms.fields import TextField, BooleanField
from wtforms.validators import Required
from myapp.models import User
from flask import g
from myapp.valiables.hoge import hoge
from flask.ext.classy import FlaskView, route


class GeneralBaseView(FlaskView):

    per_page = 5
    auth_redirect = True

    def before_request(self, name, **view_args):
        self.current_user = None
        self.is_login = False
        try:
            u = User.query.get(session['user_id'])
            self.current_user = u
            self.is_login = True
        except KeyError:
            pass
        if self.current_user is None and name != 'login' and self.auth_redirect == True:
            return redirect('/users/login', code=302)
        app.jinja_env.globals.update(
            current_user=self.current_user,
            is_login=self.is_login
        )


