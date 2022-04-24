from flask import redirect, render_template, session, request, flash
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validation(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    print(id)
    return redirect('/main')

@app.route('/login',methods=['POST'])
def login():
    user = User.grabemail(request.form)
    if not user:
        flash("Incorrect Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Incorrect Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/main')

@app.route('/main')
def main():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("main.html",user=User.grabid(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')