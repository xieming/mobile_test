from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'xxxx'
root_path = '/Users/anderson/testcode/python/flask'


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


class account(Form):
    envset = SelectField('Environment', choices=[('1', 'UAT'), ('2', 'QA'), ('3', 'STAG'), ('4', 'Live')])
    partnerset = SelectField('Partner',
                             choices=[('1', 'Cool'), ('2', 'Mini'), ('3', 'Indo'), ('4', 'Rupe'), ('5', 'Cehk'),
                                      ('6', 'Ecsp')])
    platformset = SelectField('Platform ', choices=[('1', 'V1'), ('2', 'V2')])
    typeset = SelectField('school|home', choices=[('1', 'school'), ('2', 'home')])
    levelset = SelectField('Level',
                           choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                                    ('8', '8'), ('9', '9'), ('10', '10')])
    quantityset = SelectField('Quantity', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    submit = SubmitField("Create")


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    env = None
    partner = None
    platform = None
    type = None
    level = None
    quantity = None
    Accounts = account()
    if Accounts.validate_on_submit():
        env = Accounts.envset.data
        partner = Accounts.partnerset.data
        platform = Accounts.platformset.data
        type = Accounts.typeset.data
        level = Accounts.levelset.data
        quantity = Accounts.quantityset.data
    return render_template('account.html', form=Accounts, env=env, partner=partner, platform=platform, type=type,
                           level=level, quantity=quantity)


class progress(Form):
    usernameset = StringField('User', validators=[DataRequired()])
    levelset = SelectField('Level',
                           choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                                    ('8', '8'), ('9', '9'), ('10', '10')])
    submit = SubmitField("submit")


@app.route('/progress_check', methods=['GET', 'POST'])
def progress_check():
    username = None
    level = None
    Progress = progress()
    if Progress.validate_on_submit():
        username = Progress.usernameset.data
        level = Progress.levelset.data
    return render_template('progress.html', form=Progress, username=username, level=level)


class coupon(Form):
    envset = SelectField('Environment', choices=[('1', 'UAT'), ('2', 'QA')])
    usernameset = StringField('User', validators=[DataRequired()])
    submit = SubmitField("submit")


@app.route('/coupon_check', methods=['GET', 'POST'])
def coupon_check():
    env = None
    username = None
    Coupon = coupon()
    if Coupon.validate_on_submit():
        env = Coupon.envset.data
        username = Coupon.username.data
    return render_template('coupon.html', form=Coupon, env=env, username=username)


class content(Form):
    env = SelectField('Environment', choices=[('uat', 'UAT'), ('qa', 'QA'), ('stag', 'STAG')])
    product = SelectField('Product', choices=[('b2c', 'B2C'), ('b2b', 'B2B'), ('ec', 'EC')])
    username = StringField('User', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField("Check")


@app.route('/content_check')
def content_check():
    env = None
    product = None
    user = None
    pwd = None
    Content = content()
    if Content.validate_on_submit():
        env = Content.env.data
        product = Content.product.data
        user = Content.username.data
        pwd = Content.password.data
    return render_template('content.html', form=Content, env=env, product=product, user=user, pwd=pwd)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
    # app.debug = True
    # app.run("0.0.0.0", port = 5000)
