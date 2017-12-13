
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite://C:/Users/Joshu/Programming/SmartVet/data/test.db"
    SECRET_KEY = "James Bond"
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_RECOVERABLE = False
    SECURITY_REGISTER_USER_TEMPLATE = "security/register_user.html"
    SECURITY_LOGIN_USER_TEMPLATE = "security/login_user.html"
    SECURITY_POST_LOGIN_VIEW = "/dashboard/"
    SECURITY_POST_LOGOUT_VIEW = "/login/"
    SECURITY_POST_REGISTER_VIEW = "/login/"
    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"
    SECURITY_REGISTER_URL = "/register/"
    SECURITY_UNAUTHORIZED_VIEW = "/unauthorised/"
    SECURITY_PASSWORD_HASH = "sha512_crypt"



class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True

