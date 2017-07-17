# A sample of Python MVC pattern using Flask framework.

Demo :[http://172.104.82.128/](http://172.104.82.128/)

## Constitution

Framework : Flask 0.11.1
ORM : SQLAlchemy
Templete engine : jinja template
Python 3.6.0

... and more, please see requirement.txt

## Installation & Preparetion


`$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv`

`$ git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv`

`$ vi .zshrc`

```
# For Python Environment
export PYTHON_ROOT="${HOME}/.pyenv"
if [ -d "${PYTHON_ROOT}" ]; then
   export PATH=${PYTHON_ROOT}/bin:$PATH
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
fi
```

`$ source .zshrc`

※ All you have to do is setting up to be able to use `pyenv` command. It does not matter if you do not need the above method.

`$ sudo apt-get install libssl-dev libbz2-dev`

`$ pyenv install 3.6.0`

`$ pyenv rehash`

`$ pyenv global 3.6.0`

`$ python --version`

`$ git clone https://github.com/bamboo-yujiro/flask-mvc-sample.git /path/to/`

`$ cd /path/to/`

`$ sudo apt-get install mysql-client mysql-server`

`$ sudo apt-get install libcurl4-gnutls-dev`

`$ sudo apt-get install libmysqlclient-dev`

`$ pyenv virtualenv 3.6.0 flask-mvc-sample`

`$ pyenv activate flask-mvc-sample`

`$ pip install -r requirements.txt`

`$ python migrate.py db upgrade`

`$ cp env.py.sample env.py.sample `

`$ vi env.py`

※ before this, create database, and then rewrite env.py

`$ python main.py`

=> running server!

