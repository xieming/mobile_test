import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'xxxx'
app.config['UPLOAD_FOLDER'] = 'uploads/'
root_path = '/Users/anderson/testcode/python/flask'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','apk','ipa'])

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
    partnerset = SelectField('Partner', choices=[('1', 'Cool'), ('2', 'Mini'), ('3', 'Indo'), ('4', 'Rupe'), ('5', 'Cehk'), ('6', 'Ecsp')])
    platformset = SelectField('Platform ', choices=[('1', 'V1'), ('2', 'V2')])
    typeset = SelectField('school|home', choices=[('1', 'school'), ('2', 'home')])
    levelset = SelectField('Level', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
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
    return render_template('account.html', form=Accounts, env=env, partner=partner, platform=platform,type=type,level=level,quantity=quantity)
#@app.route('/account')
#def account():
#    return render_template('account.html')
@app.route('/signin', methods=['POST'])
def signin():
    #receive the data from submit
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)

class progress(Form):
    usernameset = StringField('User', validators=[DataRequired()])
    levelset = SelectField('Level', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
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
        username= Coupon.username.data
    return render_template('coupon.html', form=Coupon, env=env,username=username)


def allowed_file(filename):
  return '.' in filename and \
      filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/up')
def up():
  return render_template('up.html')
# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
  # Get the name of the uploaded files
  uploaded_files = request.files.getlist("file[]")
  filenames = []
  for file in uploaded_files:
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
      # Make the filename safe, remove unsupported chars
      filename = secure_filename(file.filename)
      # Move the file form the temporal folder to the upload
      # folder we setup
      file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      # Save the filename into a list, we'll use it later
      filenames.append(filename)
      # Redirect the user to the uploaded_file route, which
      # will basicaly show on the browser the uploaded file
  # Load an html page with a link to each uploaded file
  return render_template('upload.html', filenames=filenames)

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#   return send_from_directory(app.config['UPLOAD_FOLDER'],
#                 filename)

from flask import request,jsonify,send_from_directory,abort

@app.route('/down_loads')
def down_loads():
    if request.method=="GET":
        if os.listdir(os.path.join('uploads')):
            files = os.listdir(os.path.join('uploads'))
            return render_template('down_loads.html',files=files)
        abort(404)

# @app.route('/uploads/<path:filename>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                    filename, as_attachment=True)

# def download(filename):
#     if request.method=="GET":
#         if os.path.isfile(os.path.join('upload', filename)):
#             return send_from_directory('upload',filename,as_attachment=True)
#         abort(404)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename,as_attachment=True)

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
    return render_template('content.html', form=Content, env=env, product=product, user=user,pwd=pwd)

@app.route('/content_check', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        env = request.form['env']
        product = request.form['product']
        return env+'</br>'+product

    #return render_template('progress.html',env)


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port = 5000)
    # app.debug = True
    # app.run("0.0.0.0", port = 5000)