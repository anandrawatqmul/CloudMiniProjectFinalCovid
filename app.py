__author__ = "Anand Rawat"
from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from covid import getCountryData
from cassandra.cluster import Cluster
cluster = Cluster(contact_points=['172.17.0.2'],port=9042)
csession = cluster.connect()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    """ Here we are creating User table to maintain database for username and password"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/', methods=['GET', 'POST'])
def home():
    """ This is the function for Session control"""
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        if request.method == 'POST':
            country = request.form['country']
            return render_template('index.html', data=getCountryData(country))
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Funtion for Login Form"""
    if (request.method == 'GET' or request.method == 'PUT'):
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=passw).first()
            if data is not None:
                session['logged_in'] = True
                session['username'] = name
                return redirect(url_for('home'))
            else:
                return 'Wrong Username or Password'
        except:
            return "Dont Login"


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Funtion for registration form"""
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is not None:
            return render_template('register.html', data="Username Already Exists")
        new_user = User(
            username=request.form['username'],
            password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')


@app.route('/forgot/', methods=['GET', 'PUT'])
def forgot():
    """Registration Form """
    if request.method == 'PUT':
        username = request.json['username']
        password = request.json['password']
        user = User.query.filter_by(username=username).first()
        user.password = password
        db.session.commit()
        return render_template('forgot.html')
    return render_template('forgot.html')


@app.route('/deactivate/', methods=['DELETE'])
def deactivate():
    """Registration Form"""
    if request.method == 'DELETE':
        session['logged_in'] = False
        username = session['username']
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        return {'success': True}
    return {'success': False}

"""Logout Form"""
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.secret_key = "123"
    app.run(host='0.0.0.0')
    
