from flask import Flask,render_template,flash
from app import app
from .models import Users

from .form import NameForm,UserForm

from . import db


@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/user/<name>')
def user(name):
    return  render_template ('user.html', name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/name',methods = ['GET','POST'])
def name():
    name= None
    form = NameForm()
    if form.validate_on_submit():
       name = form.name.data
       form.name.data = ''
       flash('Form submitted successfuly')

    return render_template('name.html', name = name , form = form)

@app.route('/user/add',methods = ['GET','POST'],)
def add_user():
    name= None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email = form.email.data).first()
        if user is None:
            user=Users(name=form.name.data,email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data=''
        form.email.data=''
        flash('User added successfuly')
    our_users=Users.query.order_by(Users.date_added)

    return render_template('add_user.html',form=form,name=name,our_users=our_users)