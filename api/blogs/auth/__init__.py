from flask import Blueprint
from flask_restful import Api
from .views import RegisterView, LoginView

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
blog_api = Api(auth)

blog_api.add_resource(RegisterView, '/register')
blog_api.add_resource(LoginView, '/login')