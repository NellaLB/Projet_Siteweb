from flask import Flask, abort, render_template
from markupsafe import escape
import datetime

app = Flask(__name__) #Instance

@app.route('/') #Décorateur : Instruction définissant URL
@app.route('/index/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/capitadd/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/addition/<int:nb1>/<int:nb2>/')
def addition(nb1,nb2):
    try:
        return '<h2>{}</h2>'.format(nb1 + nb2)
    except IndexError:
        abort(404)

@app.route('/comments/')
def comments():
    comments = [
        'You can add two numbers with : /addition/n1/n2',
        'You can have a name with : /capitalize/'
    ]
    return render_template('comments.html',comments=comments)