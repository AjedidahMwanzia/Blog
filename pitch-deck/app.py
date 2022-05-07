from flask import Flask, render_template

# create an instance
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello Wolrd'
