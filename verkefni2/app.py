import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('default.html')


@app.route('/ktsida/<kt>')
def ktsida(kt):
    summa=0
    for item in kt:
        summa=summa+int(item)
    return render_template('kt-sum.html',summa=summa,kt=kt)


@app.errorhandler(404)
def YOUWERETHECHOSENONE(error):
    return render_template('NOOYOUWERETHECHOSENONE.html'),404


if __name__ == "__main__":
    app.run(debug=True)