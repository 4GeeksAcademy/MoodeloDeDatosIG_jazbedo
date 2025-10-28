from flask_sqlalchemy import SQLAlchemy
f

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image_url = db.Column(db.String(250))
    caption = db.Column(db.String(250))

    def __repr__(self):
        return f'<Post {self.id}>'
    
class Comment(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.string(250))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post_id'))

    def __repr__(self):
        return f'<Post {self.id}>'
    
class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_from_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_to_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Follower {self.user_from_id} -> {self.user_to_id}>'

