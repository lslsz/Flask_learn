from flask import Flask, request, redirect, abort, make_response, jsonify, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'ABC_DDDK13Dsje24')

@app.route('/')
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
        response = '<h1>Hello, %s!</h1>' % name
        if 'logged_in' in session:
            response += '[Authenticated]'
        else:
            response += '[Not Authenticated]'
        return response

@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d!</p>' % (2018 - year)

@app.route('/colors/<any(blue, white, red):color>')
def colors(color):
    return '<p>%s</p>' % color

@app.route('/redirect')
def re():
    return redirect('http://www.example.com')

@app.route('/404')
def not_found():
    abort(404)

@app.route('/foo')
def foo():
    return jsonify(name='sllin', gender='male')

@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response

@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))
