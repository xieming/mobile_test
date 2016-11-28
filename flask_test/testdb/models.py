#encoding=utf-8
from app import db
from datetime import datetime

class Message(db.Model):
        __tablename__ ="message"
        id = db.Column(db.Integer,primary_key=True)
        name = db.Column(db.String(200))
        time = db.Column(db.DateTime,default=datetime.now())
        content = db.Column(db.String(255))
        email = db.Column(db.String(100))
        title = db.Column(db.String(255))

        def __init__(self,name,content,email,title):
                self.name = name
                self.content = content
                self.email = email
                self.title = title

        def __repr__(self):
                return "<User:%s>" %self.name


if __name__=="__main__":
        db.create_all()


#mysql> CREATE TABLE message(
#   -> id INT NOT NULL AUTO_INCREMENT,
#   -> name VARCHAR(200) NOT NULL,
#   -> time DATE,
#   -> content VARCHAR(255) NOT NULL,
#   -> email VARCHAR(100) NOT NULL,
#   -> title VARCHAR(255) NOT NULL,
#   -> PRIMARY KEY ( id )
#   -> );