from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
# SQLAlchemy ve Flask-Migrate genişletmelerini başlatma
db = SQLAlchemy(app)
migrate = Migrate(app, db)