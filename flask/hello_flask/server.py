from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html")  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/hi/<string:name>')
def hi(name):
    print(name)
    return " Hi " + name

@app.route('/repeat/<string:word>/<int:num>')
def repeat(word, num):
    print(word, num)
    return f"{word * num}"

if __name__=="__main__":
    app.run(debug=True)