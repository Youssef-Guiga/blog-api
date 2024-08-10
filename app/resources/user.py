from flask_restful import Resource, reqparse
from app.models import User
from app.schemas import user_schema
from app.extensions import db, bcrypt
from flask_jwt_extended import create_access_token

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help="Username cannot be blank")
user_parser.add_argument('password', type=str, required=True, help="Password cannot be blank")

class UserRegister(Resource):
    def post(self):
        """
        Register a new user
        ---
        tags:
          - Authentication
        parameters:
          - in: body
            name: body
            schema:
              type: object
              required:
                - username
                - password
              properties:
                username:
                  type: string
                  description: The user's username.
                password:
                  type: string
                  description: The user's password.
        responses:
          201:
            description: User created successfully
          400:
            description: User already exists
        """
        data = user_parser.parse_args()
        if User.query.filter_by(username=data['username']).first():
            return {"message": "User already exists"}, 400
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created successfully"}, 201

class UserLogin(Resource):
    def post(self):
        """
        User login
        ---
        tags:
          - Authentication
        parameters:
          - in: body
            name: body
            schema:
              type: object
              required:
                - username
                - password
              properties:
                username:
                  type: string
                  description: The user's username.
                password:
                  type: string
                  description: The user's password.
        responses:
          200:
            description: Login successful
          401:
            description: Invalid credentials
        """
        data = user_parser.parse_args()
        user = User.query.filter_by(username=data['username']).first()
        if user and bcrypt.check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200
        return {"message": "Invalid credentials"}, 401
