import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SECRET_KEY = 'dont_tell_anyone'
SQLALCHEMY_TRACK_MODIFICATIONS = False

GOOGLE_CLIENT_ID = "664926608124-3dd9atkiujmgdr1kg38ag1orr1f4kbuj.apps.googleusercontent.com"
GOOGLE_CLINT_SECRET = "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"
SECRET_KEY = 'dont_tell_anyone'
OAUTHLIB_INSECURE_TRANSPORT = "1"
OAUTHLIB_RELAX_TOKEN_SCOPE = "1"