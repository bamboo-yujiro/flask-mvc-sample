from myapp.controllers import *
from flask_wtf import Form
from wtforms import validators
from wtforms.fields import TextField, PasswordField
from wtforms.validators import Required, ValidationError
from myapp.models import User
from flask import g
from myapp.valiables.hoge import hoge
from myapp.controllers.general_base import GeneralBaseView
from werkzeug.security import generate_password_hash, check_password_hash


class UsersView(GeneralBaseView):

    route_base='/'
    per_page = 5
    no_auth_redirect_actions = ['logout', 'create']

    def before_request(self, name, **view_args):
        if name in self.no_auth_redirect_actions:
            self.auth_redirect = False
        return super().before_request(name, **view_args)

    @route('/users/login', methods=['GET', 'POST'])
    def login(self):
        if request.method == 'POST':
            username=request.form['username']
            password=request.form['password']
            u = User.query.filter(User.username == username).first()
            if u is not None:
                if check_password_hash(u.password, password) :
                    session['user_id'] = u.id
                    return redirect('/')
            flash('User name or password is incorrect.')
        return render_template('users/login.html')


    @route('/users/logout')
    def logout(self):
        session.pop('user_id', None)
        flash('Logged out.')
        return redirect('/')

    @route('/users/create', methods=['GET', 'POST'])
    def create(self):
        form = Registration(request.form)
        if request.method == 'POST' and form.validate():
            user = User(username=form.username.data,password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            flash('You are registered.')
            return redirect('/users/login')
        return render_template('users/create.html', form=form)


def uniq(form,field):
    user = User.query.filter(User.username == field.data).first()
    if user is not None:
        raise ValidationError('The entered user already exists.')
    return True

class Registration(Form):
    username = TextField('Username', [
        validators.Length(min=4, max=20, message='User name must be 4 or more characters and 25 characters or less.'),
        uniq
    ])
    password = PasswordField('Password', [
        validators.Required(message='This is required field.'),
        validators.Length(min=8, max=20, message='Password should be 8 or more characters and 20 characters or less.'),
        validators.EqualTo('confirm', message='Passwords do not match.')
    ])
    confirm = PasswordField('Retype password')
