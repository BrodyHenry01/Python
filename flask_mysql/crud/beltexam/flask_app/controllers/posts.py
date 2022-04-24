from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.post import Post
from flask_app.models.user import User


@app.route('/new/post')
def new_post():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('sightings.html',user=User.grabid(data))


@app.route('/create/post',methods=['POST'])
def create_post():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/new/post')
    data = {
        "username": request.form["username"],
        "description": request.form["description"],
        "location": request.form["location"],
        "squatches": int(request.form["squatches"]),
        "date_of": request.form["date_of"],
        "user_id": session["user_id"]
    }
    Post.save(data)
    return redirect('/dashboard')

@app.route('/edit/post/<int:id>')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit.html",edit=Post.get_one(data),user=User.grabid(user_data))

@app.route('/update/post',methods=['POST'])
def update_post():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/new/post')
    data = {
        "username": request.form['username'],
        "description": request.form["description"],
        "location": request.form["location"],
        "squatches": int(request.form["squatches"]),
        "date_of": request.form["date_of"],
        "id": request.form['id']
    }
    Post.update(data)
    return redirect('/dashboard')

@app.route('/post/<int:id>')
def show_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show.html",post=Post.get_one(data),user=User.grabid(user_data))

@app.route('/remove/post/<int:id>')
def remove_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Post.remove(data)
    return redirect('/dashboard')