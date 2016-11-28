from flask import render_template, flash, redirect
from forms import LoginForm
from app import app

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Name: ' + form.name.data)
        flash('passwd: ' + str(form.password.data))
        flash('remember_me: ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In',form = form)
    