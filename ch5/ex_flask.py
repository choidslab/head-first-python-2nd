from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Flask!'

@app.route('/dslab')
def intro_dslab():
    return '안녕하세요. DSLab에 오신 것을 환영합니다. :)'

app.run()  # flask web server 실행
