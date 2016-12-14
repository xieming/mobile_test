from flask import Flask, render_template,request,flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from account_ec import AccountHelper
from config import Environment
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:@localhost:3306/info"
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'xxxx'
root_path = '/Users/anderson/testcode/python/flask'
from models import *



# urls = (
#     '/', 'index',
#     '/favicon.ico', 'icon'
# )
#
# # Process favicon.ico requests
# class icon:
#     def GET(self): raise web.seeother("/static/favicon.ico")

@app.route('/')
def index():

    return render_template('index.html')


class account_form(Form):
    envset = SelectField('Environment', choices=[('uat', 'UAT'), ('qa', 'QA'), ('stag', 'STAG')])
    partnerset = SelectField('Partner',
                             choices=[('cool', 'Cool'), ('mini', 'Mini'), ('indo', 'Indo'), ('rupe', 'Rupe'), ('cehk', 'Cehk'),
                                      ('ecsp', 'Ecsp')])
    platformset = SelectField('Platform ', choices=[('v1', 'V1'), ('v2', 'V2')])
    typeset = SelectField('school|home', choices=[('school', 'school'), ('home', 'home')])
    levelset = SelectField('Level',
                           choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                                    ('8', '8'), ('9', '9'), ('10', '10')])
    quantityset = SelectField('Quantity', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    submit = SubmitField("Create")


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    form = account_form(request.form)
    if request.method == "POST":
        current_env = form.envset.data
        current_partner = form.partnerset.data
        current_platform = form.platformset.data
        current_type = form.typeset.data
        current_level = form.levelset.data
        current_quantity = form.quantityset.data
        #account = (form.envset.data,form.partnerset.data,form.platformset.data,form.typeset.data,form.levelset.data,form.quantityset.data)

        productId = INFO.query.filter_by(Partner= current_partner)
        # divisionCode = INFO.query.filter_by(Partnerf=current_partner).third()
        # mainRedemptionCode = INFO.query.filter_by(Partner=current_partner).fourth()
        # freeRedemptionCode = INFO.query.filter_by(Partner=current_partner).fifth()

        # account_info = AccountHelper(Environment.get_host(current_env))
        # memberId = account_info.create_member()
        #
        # result = account_info.set_values(memberId, mainRedemptionCode, freeRedemptionCode, divisionCode, productId)

        return 'Hello %s !' % INFO.query.filter_by(Partner='cool').first()
    else:
        return render_template('account.html',form = form)

    # env = None
    # partner = None
    # platform = None
    # type = None
    # level = None
    # quantity = None
    # Accounts = account()
    # if Accounts.validate_on_submit():
    #     flash('please wait: ')
    #     env = Accounts.envset.data
    #     partner = Accounts.partnerset.data
    #     platform = Accounts.platformset.data
    #     type = Accounts.typeset.data
    #     level = Accounts.levelset.data
    #     quantity = Accounts.quantityset.data
    #
    #
    # # # memberId= account_info.create_member()
    # # mainRedemptionCode = "S15SCHOOLMAIN"
    # # freeRedemptionCode = "S15SCHOOLF1D"
    # # divisionCode = "SSCNTE2"
    # # productId = 63

    # result = account_info.set_values(memberId, mainRedemptionCode, freeRedemptionCode, divisionCode, productId)

    # return render_template('account.html', form=Accounts, env=env, partner=partner, platform=platform, type=type,
    #                        level=level, quantity=quantity)

# @app.route('/create_account', methods=['GET', 'POST'])
# def create_account():
#     current_env = request.form['env']
#     current_partner = request.form['partner']
#     current_platform = request.form['platform']
#     current_type = request.form['type']
#     current_level = request.form['level']
#     current_quantity = request.form['quantity']
#
#     productId = INFO.query.filter_by(Partner=current_partner).second()
#     divisionCode = INFO.query.filter_by(Partnerf=current_partner).third()
#     mainRedemptionCode = INFO.query.filter_by(Partner=current_partner).fourth()
#     freeRedemptionCode = INFO.query.filter_by(Partner=current_partner).fifth()
#
#     account_info = AccountHelper(Environment.get_host(current_env))
#     memberId = account_info.create_member()
#
#     result = account_info.set_values(memberId, mainRedemptionCode, freeRedemptionCode, divisionCode, productId)
#
#     #return request.form['name']+'</br>'+request.form['passwd']
#     return render_template('index.html')





if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
    # app.debug = True
    # app.run("0.0.0.0", port = 5000)
