#encoding=utf-8
# from  flask import Flask
# import MySQLdb
# from app import app
#
# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
from app import db


# app = Flask(__name__)
# track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
# app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:@localhost:3306/info"
# db = SQLAlchemy(app)

class INFO(db.Model):
        __tablename__ ="info"
        #id = db.Column(db.Integer,primary_key=True)
        Partner = db.Column(db.String(200),primary_key=True)
        #time = db.Column(db.DateTime,default=datetime.now())
        Product_ID = db.Column(db.Integer)
        Product_Name = db.Column(db.String(100))
        MainRedemptionCode = db.Column(db.String(255))
        FreeRedemptionCode = db.Column(db.String(255))

        def __init__(self,Partner,Product_ID,Product_Name,MainRedemptionCode,FreeRedemptionCode):
                self.Partner = Partner
                self.Product_ID = Product_ID
                self.Product_Name = Product_Name
                self.MainRedemptionCode = MainRedemptionCode
                self.FreeRedemptionCode = FreeRedemptionCode

        def __repr__(self):
                return "<Partner:%s>" %self.Partner


if __name__=="__main__":
        db.create_all()