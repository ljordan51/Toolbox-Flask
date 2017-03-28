"""
Put your Flask app code here.
"""

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    age = request.form['age']
    ninja = request.form['ninja']
    if name and age and ninja:
        return render_template('login.html', name=name, age=age, error=False)
    else:
        return render_template('login.html', error=True)


if __name__ == '__main__':
    app.run()
