import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'password1'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	MAIL_SERVER = 'localhost'
	MAIL_PORT = 25
	MAIL_USE_TLS = False
	MAIL_USE_SSL = False 
	MAIL_USERNAME = None
	MAIL_PASSWORD = None
	MAIL_DEFAULT_SENDER = 'jack@jack.com'
	ADMINS = ['jack@jack.com']
	POSTS_PER_PAGE = 25
	LANGUAGES = ['en-US', 'es']
	MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
	
