import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    print(SECRET_KEY)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your email address' 
    MAIL_PASSWORD = 'your email password'
    # or replace 'your email address' and 'your email password'
    # with os.environ.get(MAIL_USERNAME) if you have your secret
    # information stored in .bash_profile.txt.