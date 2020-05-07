# from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request
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

    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)


@app.route('/')  # Flask에서 함수는 여러개의 URL 값을 가질 수 있다. decorator를 통해서!
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the DSLab web!')


if __name__ == "__main__":
    app.run(debug=True)  # debug mode on

