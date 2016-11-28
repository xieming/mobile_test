from flask import Flask, render_template, flash, redirect
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Name: ' + form.name.data)
        flash('passwd: ' + str(form.password.data))
        flash('remember_me: ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In',form = form)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    