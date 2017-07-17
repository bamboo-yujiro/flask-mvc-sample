import sys
from flask import Flask
from flask_script import Server, Command, Option
import feedparser
import logging
import logging.config
from app import app
from myapp.management.commands import logs
import datetime

class BaseCommand(Command):

    def __init__(self):
        """ 子クラスで定義されたログの名前でlogging 登録する """
        todaydetail = datetime.datetime.today()
        d = todaydetail.strftime("%Y%m%d")
        logName = d + '_' + self.logPrefix
        logs.init_app(app, logName)


    def info(self, msg):
        app.logger.info(msg)
        print(msg)

    def error(self, msg):
        app.logger.error(msg)
        print(msg)
        sys.exit()

