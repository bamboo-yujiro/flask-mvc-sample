import sys
from flask import Flask
from flask_script import Server, Manager

app = Flask(__name__)

manager = Manager(app)
args = sys.argv
prePath = 'myapp.management.commands.'
batName = args[1]
batFile = prePath + batName
clsName = (batName[0]).upper() + batName[1:]

exec("from %s import %s"%(batFile, clsName))

manager.add_command("crawl", Crawl())

if __name__ == "__main__":
    manager.run()
