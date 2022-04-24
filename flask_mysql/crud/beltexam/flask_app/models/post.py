from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
    db = 'beltschema'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.username = db_data['username']
        self.description = db_data['description']
        self.location = db_data['location']
        self.squatches = db_data['squatches']
        self.date_of = db_data['date_of']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO posts (username, description, location, squatches, date_of, user_id) VALUES (%(username)s,%(description)s,%(location)s,%(squatches)s,%(date_of)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_posts = []
        for row in results:
            print(row['date_of'])
            all_posts.append( cls(row) )
        return all_posts
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM posts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET username=%(username)s,description=%(description)s, location=%(location)s, squatches=%(squatches)s, date_of=%(date_of)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def remove(cls,data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['username']) < 3:
            is_valid = False
            flash("username must be at least 3 characters","post")
        if len(post['location']) < 3:
            is_valid = False
            flash("location must be at least 3 characters","post")
        if len(post['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","post")
        if post['date_of'] == "":
            is_valid = False
            flash("Please enter a date","post")
        if int(post['squatches']) < 1:
            is_valid = False
            flash('You gotta see atleast one Sasquatch to report it', "post")
        return is_valid