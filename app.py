from flask import Flask, abort, render_template, session, app, request, url_for,redirect
from markupsafe import escape
import datetime

app = Flask(__name__) #Instance
app.secret_key =  b'_5#y2L"F4Q8z\n\xec]/' #Eviter piratage


@app.route('/') #Décorateur : Instruction définissant URL
@app.route('/index/')
def hello():
    if ('username' in session) and ('password' in session):
        return render_template('index.html', utc_dt=datetime.datetime.utcnow())
    return redirect(url_for('login'))



@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if session['username'] == 'John' and session['password'] == '1234':
            return redirect(url_for('hello'))
        else:
            return redirect(url_for('login'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('hello'))





@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/capitaze/<word>/')
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

if __name__ == '__main__':
    app.run()