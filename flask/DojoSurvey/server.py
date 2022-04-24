from flask import Flask, redirect, render_template, request, session


app = Flask(__name__)

app.secret_key="password"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['cohort'] = request.form['cohort']
    session['game'] = request.form['game']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)