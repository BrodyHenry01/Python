from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",width=8,height=8,color='red',color_two='blue')

@app.route('/<int:x>')
def row(x):
    return render_template("index.html",width=x,hieght=8,color='red',color_two='blue')

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("index.html",width=x,height=y,color='red',color_two='blue')



if __name__=="__main__":
    app.run(debug=True)