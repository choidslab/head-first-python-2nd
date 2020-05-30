# from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request, escape
from ch4.vsearch2 import search4letters
from ch9.dbcm import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


@app.route('/dslab')
def intro_dslab():
    return '안녕하세요. DSLab에 오신 것을 환영합니다. :)'


@app.route('/search4', methods=['POST'])
def do_search():
    """Return a set of the 'letters' found in 'phrases'."""
    # return str(search4letters('life, the universe, and everything', 'eiru'))
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)

    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)


@app.route('/')  # Flask에서 함수는 여러개의 URL 값을 가질 수 있다. decorator를 통해서!
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the DSLab web!')


@app.route('/viewlog')
def view_log():

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results 
                  from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase', 'Letters', 'Remote_IP_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log', the_row_titles=titles, the_data=contents)


def log_request(req, res):
    # with open('./vsearch.log', 'a') as vlog:
    #     print(req.form, req.remote_addr, req.user_agent, res, file=vlog, sep=' | ')

    with UseDatabase(app.config['dbconfig']) as cursor:  # context manager
        _SQL = """insert into log(phrase, letters, ip, browser_string, results) values(%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res))

    # conn = mysql.connector.connect(**dbconfig)
    # cursor = conn.cursor()
    # conn.commit()
    # cursor.close()
    # conn.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')  # 외부 접속 가능하도록 설정
