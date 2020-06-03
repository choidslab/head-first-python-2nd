""" Head First Python 2nd - ch10 source code """

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'Simple Webapp'


@app.route('/')
def hello():
    return 'Hello from the simple webapp!'


@app.route('/login')
def do_login():
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout():
    # del session['logged_in']  # logged_in key 삭제 --> 내가 한 방식
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/status')
def check_status():
    if 'logged_in' in session.keys(): # session dict에 'logged_in' key가 있는지 확인
        return 'You are currently logged in'
    return 'You are Not logged in!'


@app.route('/page1')
def page1():
    return 'This is page 1.'


@app.route('/page2')
def page2():
    return 'This is page 2.'


@app.route('/page3')
def page3():
    return 'This is page 3.'


if __name__ == "__main__":
    app.run(debug=True)
