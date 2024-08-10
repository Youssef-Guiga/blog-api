from flask_restful import Api
from app.resources.user import UserRegister, UserLogin
from app.resources.post import PostResource, PostListResource

def create_resources(app):
    api = Api(app)
    
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(PostListResource, '/posts')
    api.add_resource(PostResource, '/posts/<int:post_id>')
