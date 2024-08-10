from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flasgger import Swagger

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
ma = Marshmallow()
swagger = Swagger()
