# from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request, escape
from ch4.vsearch2 import search4letters
app = Flask(__name__)


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
    contents = list()
    with open('./vsearch.log', 'r') as viewlog:
        for line in viewlog:
            contents.append([])
            for item in line.split(' | '):
                contents[-1].append(escape(item))
            # print(contents)
    titles = ('Form Data', 'Remote_IP_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View Log', the_row_titles=titles, the_data=contents)

def log_request(req, res):
    with open('./vsearch.log', 'a') as vlog:
        print(req.form, req.remote_addr, req.user_agent, res, file=vlog, sep=' | ')


if __name__ == "__main__":
    app.run(debug=True)  # debug mode on

