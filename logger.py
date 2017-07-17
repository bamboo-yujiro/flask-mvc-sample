import os
import sys
from app import app
import logging
from logging.handlers import RotatingFileHandler

class LevelFilter(logging.Filter):
    """
    http://stackoverflow.com/a/7447596/190597 (robert)
    """
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level

def not_exist_makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def common(path_list):
    print(path_list)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    )
    debug_log = path_list['debug']
    not_exist_makedirs(os.path.dirname(debug_log))

    debug_file_handler = RotatingFileHandler(
        debug_log, maxBytes=1000000, backupCount=10
    )

    debug_file_handler.addFilter(LevelFilter(logging.DEBUG))
    #debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)

    error_log = path_list['error']
    not_exist_makedirs(os.path.dirname(error_log))
    error_file_handler = RotatingFileHandler(
        error_log, maxBytes=1000000, backupCount=10
    )
    error_file_handler.addFilter(LevelFilter(logging.ERROR))
    #error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)

    app.logger.propagate = False

    app.logger.setLevel(logging.DEBUG) ##


# from general TODO
def regist(app):
    d = os.path.join(app.root_path, 'logs/debug.log')
    e = os.path.join(app.root_path, 'logs/error.log')
    path_list = {
        'debug': d,
        'error': e
    }
    common(path_list)

# from management TODO
def regist_bat(app, log_name):
    d = os.path.join(app.root_path, 'logs/%s_debug.log'% log_name)
    e = os.path.join(app.root_path, 'logs/%s_error.log'% log_name)
    path_list = {
        'debug': d,
        'error': e
    }
    common(path_list)


