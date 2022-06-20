import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SECRET_KEY = 'dont_tell_anyone'
SQLALCHEMY_TRACK_MODIFICATIONS = False


OAUTHLIB_INSECURE_TRANSPORT = "1"
OAUTHLIB_RELAX_TOKEN_SCOPE = "1"