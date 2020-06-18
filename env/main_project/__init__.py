from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# MUST BE UPDATED ON RELEASE
app.config['SECRET_KEY'] = 'b9457a3518aa6d425fff061cbd1678406698da0dc218abffc\
                            d6cc19820a431a8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from main_project import routes