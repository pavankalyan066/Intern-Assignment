from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def getvalue():
    name = request.form['name']
    number = request.form['number']
    ug = request.form['UG']
    ugyear = request.form['UGYear']
    pg = request.form['PG']
    pgyear = request.form['PGYear']
    python = request.form['python']
    r = request.form['r']
    ds = request.form['ds']
    ml = request.form['ml']
    dl = request.form['dl']
    nlp = request.form['nlp']
    sm = request.form['sm']
    aws = request.form['aws']
    sql = request.form['sql']
    excel = request.form['excel']

    succ = str
    fail = str
    score = 0
    tot = 0
    if ug == 'Bachelor of Engineering (B.E)' or ug == 'Bachelor of Technology (B.Tech)':
        if int(ugyear) == 2020:
            score = score + 10
        elif int(ugyear) == 2019:
            score = score + 8
        elif int(ugyear) <= 2018:
            score = score + 5
        else:
            score = score + 0
    elif pg == 'Master of Science (M.Sc)' or pg == 'Master of Technology (M.Tech)':
        if int(pgyear) == 2020:
            score = score + 7
        elif int(pgyear) <= 2019:
            score = score + 3
        else:
            score = score + 0
    else:
        score = score + 0
    tot = tot + score
    print(tot)
    if python == 3:
        score = score + 10
    elif python == 2:
        score = score + 7
    elif python == 1:
        score = score + 3
    tot = tot + score
    print(tot)
    if r == 3:
        score = score + 10
    elif r == 2:
        score = score + 7
    elif r == 1:
        score = score + 3
    tot = tot + score
    print(tot)
    if ds == 3:
        score = score + 10
    elif ds == 2:
        score = score + 7
    elif ds == 1:
        score = score + 3
    tot = tot + score
    print(tot)
    if ml == 'Machine Learning' or dl == 'Deep Learning' or nlp == 'Natural Language Processing(NLP)' or sm == 'Statistical Modeling' or excel == 'MS EXCEL' or aws == 'AWS' or sql == 'SQL/NoSQL':
        tot = tot + 3
        print(tot)
    if tot > 40:
        print("pass")
        succ = 'Congratualtions'
    else:
        print("fail")
        fail = 'Better luck next time'
    return render_template('pass.html', name=name, number=number, ug=ug, ugyear=ugyear, pg=pg, pgyear=pgyear,
                           python=python, r=r, ds=ds, ml=ml, dl=dl, nlp=nlp, sm=sm, excel=excel, aws=aws, sql=sql, correct=succ, wrong=fail)


if __name__ == '__main__':
    app.run(debug=True)
