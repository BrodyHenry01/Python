from flask import Flask, redirect, render_template, request, session
import random

app = Flask(__name__)

app.secret_key="password"

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def answer(): 
    session['guess'] = int(request.form['guess'])
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)