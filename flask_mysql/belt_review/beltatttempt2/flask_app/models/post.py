from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
    db = 'arbortrary'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.species = db_data['species']
        self.reason = db_data['reason']
        self.location = db_data['location']
        self.date_planted = db_data['date_planted']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO posts (species, reason, location, date_planted, user_id) VALUES (%(species)s,%(reason)s,%(location)s,%(date_planted)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_posts = []
        for row in results:
            print(row['date_planted'])
            all_posts.append( cls(row) )
        return all_posts
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM posts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET species=%(species)s,reason=%(reason)s, location=%(location)s, date_planted=%(date_planted)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def remove(cls,data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

#trying to pull up first name from a selected post for dashboard and show
    # @classmethod
    # def get_all_posts_with_creator(cls):
    #     query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id;"
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     all_posts = []
    #     for row in results:
    #         one_post = cls(row)
    #         one_posts_author_info = {  
    #             "id": row['user.id'], 
    #             "first_name": row['first_name'],
    #         }
    #         author = user.User(one_posts_author_info)
    #         one_post.creator = author
    #         all_posts.append(one_post)
    #     return all_posts

    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['species']) < 3:
            is_valid = False
            flash("species must be at least 3 characters","post")
        if len(post['location']) < 3:
            is_valid = False
            flash("location must be at least 3 characters","post")
        if len(post['reason']) < 3:
            is_valid = False
            flash("reason must be at least 3 characters","post")
        if post['date_planted'] == "":
            is_valid = False
            flash("Please enter a date","post")
        return is_valid