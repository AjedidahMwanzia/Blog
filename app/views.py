from flask import Flask,render_template
from app import app
from .form import NameForm

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

    return render_template('name.html', name = name , form = form)