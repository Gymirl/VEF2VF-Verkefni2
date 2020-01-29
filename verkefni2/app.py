import os
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def heima():
    return render_template('index.html')


#verk2.1
@app.route('/verk2.1')
def home1():
    return render_template('kennitala.html')

#listi (Database)
#ID,Fyrirsögn,Frétt,Höfundur
frettir=[
    ['0','BROH','BIGGEST BRUH EVER!! MAN SAYS "BRUH" AND THE WHOLE CROWD CLAPS',"yesman.is"],
    ['1','PLACEHOLDERNAME','PLACEHOLDERNAME','PLACEHOLDERNAME.is'],
    ['2','PASS','PASS','PASS.is'],
    ['3','PASS','PASS','PASS.is']
]

#2.2hluti
@app.route('/verk2.2')
def seinnihluti():
    return render_template('frettir.html',frettir=frettir)

#frett
@app.route('/frett/<int:id>')
def news(id):
    return render_template('frett.html', frett=frettir[id], nr=id)

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