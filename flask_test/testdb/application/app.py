#encoding=utf-8
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request,flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:@localhost:3306/message"
db = SQLAlchemy(app)
SECERT_KEY="a secret key"
app.config.from_object(__name__)
app.secret_key=app.config['SECERT_KEY']
from models import Message

@app.route('/',methods=['POST','GET'])
def index():
        if request.method == 'POST':
                name = request.form['name']
                email = request.form['email']
                content = request.form['content']
                title = request.form['title']
                mess = Message(name=name,email=email,content=content,title=title)
                db.session.add(mess)
                db.session.commit()
                flash("Add Message Sucess!!")
                #return name+email+content+title
                return redirect(url_for("index"))
        else:
                mess = Message.query.all()
                return render_template("index.html",message=mess)

@app.route('/show/<int:id>')
def show(id):
        mess = Message.query.filter_by(id=id).first()
        if mess !=None:
                return render_template("show.html",message=mess)
        else:
                return redirect(url_for("index"))
