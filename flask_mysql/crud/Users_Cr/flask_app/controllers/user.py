from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.users import User

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("index.html")


@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/user/update/<int:id>')
def change(id):
    data ={ 
        "id":id
    }
    return render_template("upuser.html",user=User.grab(data))


@app.route('/user/update',methods=['POST'])
def update():
    print(request.form)
    User.updated(request.form)
    return redirect('/users')


@app.route('/user/delete/<int:id>')
def remove(id):
    data ={ 
        "id":id
    }
    User.remove(data)
    return redirect('/users')

@app.route('/user/display/<int:id>')
def display(id):
    data ={ 
        "id":id
    }
    return render_template('display.html', user=User.grab(data))