"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
DEFAULT_IMAGE = "https://www.pngitem.com/pimgs/m/80-800373_it-benefits-per-users-default-profile-picture-green.png"

def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):
    __tablename__ = 'users'


    def __repr__(self):
        p = self
        return f"<User id = {p.id} first_name = {p.first_name} last_name = {p.last_name} image_url={p.image_url}>"

    id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True)

    first_name = db.Column(db.Text,
                        nullable=False) 

    last_name = db.Column(db.Text,
                        nullable=False)  

    image_url = db.Column(db.Text,
                          nullable=False,
                          default=DEFAULT_IMAGE)                          

    def full_name(self):
        return f"{self.first_name} {self.last_name}"