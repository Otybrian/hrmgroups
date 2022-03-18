from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email  = db.Column(db.String(255), unique = True, index = True)
    secure_password = db.Column(db.String(300))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    leaves = db.relationship('Leave', backref='author', lazy=True)
    
    def is_active(self):
        return True
    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'



class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255))
    position = db.Column(db.String(5555))
    job_id = db.Column(db.String(255))
    department = db.Column(db.String(255))
    awards = db.Column(db.String(1222))
    experience = db.Column(db.String(2222))


    def save_profile(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_profile(cls,id):
        profiles= Profile.query.filter_by(id=id).all()
        return profiles

    def __repr__(self):
        return f'User {self.fullname}'

class Leave(db.Model):
    __tablename__ = 'leave'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category = db.Column(db.Text)
    content = db.Column(db.String(255))
    posted_date = db.Column(db.DateTime,  default=datetime.utcnow)
    
    

    def save_leave(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_leave(cls,id):
        leaves = Leave.query.filter_by(id=id).all()
        return leaves

    def __repr__(self):
        
        return f"Post('{self.content}', '{self.posted_date}', '{self.category}')"
