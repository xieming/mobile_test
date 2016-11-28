# encoding=utf-8

from flask_script import Manager
from application.app import app
manager = Manager(app)
app.config['DEBUG'] = True
if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    manager.run()