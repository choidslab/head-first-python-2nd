from flask import Flask
from ch4.vsearch2 import search4letters
app = Flask(__name__)


@app.route('/')  # decorator,route() 파라미터 값 = URL을 의미
def hello_world():
    return 'Hello World from Flask!'


@app.route('/dslab')
def intro_dslab():
    return '안녕하세요. DSLab에 오신 것을 환영합니다. :)'


@app.route('/search4')
def do_search():
    """Return a set of the 'letters' found in 'phrases'."""
    return str(search4letters('life, the universe, and everything', 'eiru'))


app.run()  # flask web serve
