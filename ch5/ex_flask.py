from flask import Flask

app = Flask(__name__)


@app.route('/')  # decorator,route() 파라미터 값 = URL을 의미
def hello_world():
    return 'Hello World from Flask!'

@app.route('/dslab')
def intro_dslab():
    return '안녕하세요. DSLab에 오신 것을 환영합니다. :)'


app.run()  # flask web serve
