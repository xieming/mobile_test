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

class TESTS(db.Model):
        __table_args__ = {'extend_existing': True}
        __tablename__ ="test"
        id = db.Column(db.Integer,primary_key=True)
        Partner = db.Column(db.String(200))
        #time = db.Column(db.DateTime,default=datetime.now())
        Product_ID = db.Column(db.Integer)
        Product_Name = db.Column(db.String(100))
        MainRedemptionCode = db.Column(db.String(255))
        FreeRedemptionCode = db.Column(db.String(255))

        def __init__(self,Partner,Product_ID,Product_Name,MainRedemptionCode,FreeRedemptionCode):
                #self.id = id
                self.Partner = Partner
                self.Product_ID = Product_ID
                self.Product_Name = Product_Name
                self.MainRedemptionCode = MainRedemptionCode
                self.FreeRedemptionCode = FreeRedemptionCode

        def __repr__(self):
                return "<TESTS:%s>" %self.Partner
# #
class ACCOUNT(db.Model):
        __table_args__ = {'extend_existing': True}
        __tablename__ = "account"
        id = db.Column(db.Integer,primary_key=True)
        Memberid = db.Column(db.Integer)
                        # time = db.Column(db.DateTime,default=datetime.now())
        Username = db.Column(db.String(255))
        Password = db.Column(db.String(100))
        Env = db.Column(db.String(255))
        Partner = db.Column(db.String(255))

        def __init__(self,Username,Password,Memberid,Env,Partner):
                self.Username = Username
                self.Password = Password
                self.Memberid = Memberid
                self.Env = Env
                self.Partner = Partner
        def __repr__(self):
                # return "<ACCOUNT:%s,%s,%d,%s,%s>" %(self.Username,self.Password,self.Memberid,self.Env,self.Partner)
                return "<ACCOUNT:%s>" %(self.Username)
        # return "<ACCOUNT:%s,%s,%d,%s,%s>" %(self.Username,self.Password,self.Memberid,self.Env,self.Partner)


# if __name__=="__main__":
#         db.create_all()

        # inset=TESTS(Partner='cool', Product_ID=63, Product_Name='school15',MainRedemptionCode='S15SCHOOLMAIN',FreeRedemptionCode='S15SCHOOLF1D')
        # db.session.add(inset)
        # db.session.commit()