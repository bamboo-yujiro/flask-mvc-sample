import os
from app import app
from flask_debugtoolbar import DebugToolbarExtension
from myapp.controllers.memos import MemosView
from myapp.controllers.users import UsersView
from myapp.controllers.top import TopView
import bundle
import env
import logger

MemosView.register(app)
UsersView.register(app)
TopView.register(app)

if env.env != 'production':
    app.debug = True
else:
    app.debug = False


app.debug = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'aiuoe'
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

""" logging """
logger.regist(app)

if __name__ == '__main__':
    if env.env != 'production':
        """ Auto Reload """
        extra_dirs = ['templates',]
        extra_files = extra_dirs[:]
        for extra_dir in extra_dirs:
            for dirname, dirs, files in os.walk(extra_dir):
                for filename in files:
                    filename = os.path.join(dirname, filename)
                    if os.path.isfile(filename):
                        extra_files.append(filename)
        app.run(extra_files=extra_files, host= env.host)
    else:
        app.run()

