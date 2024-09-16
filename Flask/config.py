from flask import Flask 
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345@localhost:3306/ecommerce"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = '5307af8b5240a5366c9cf3cc3c838c7fe9893f1a9e1227609091ded7e8593f46'

MAIL_SERVER = 'smtp.example.com'
MAIL_PORT = 587
MAIL_USERNAME = 'your-email@example.com'
MAIL_PASSWORD = 'your-email-password'
MAIL_USE_TLS = True
MAIL_USE_SSL = False
