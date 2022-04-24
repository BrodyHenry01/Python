from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {"first_name" : "Brody", "last_name" : "Henry"},
        {"first_name" : "Brynn", "last_name" : "Mess"},
        {"first_name" : "John", "last_name" : "Wick"},
        {"first_name" : "Brod", "last_name" : "addy"},
    ]

    return render_template("index.html", users = users)



if __name__== '__main__':
    app.run (debug=True) 