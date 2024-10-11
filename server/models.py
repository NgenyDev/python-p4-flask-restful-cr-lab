
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Fixed db.string to db.String
    image = db.Column(db.String, nullable=False, default='default_image.png')
    price = db.Column(db.Numeric(10, 2), nullable=False, default=0.0)  # Fixed db.numeric to db.Numeric
