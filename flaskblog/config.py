import os


class Config:
    SECRET_KEY = "oijxijxiaxhsah"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ayushi1412@localhost:5432/flaskblogapp"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ag.codeash14@gmail.com'
    MAIL_PASSWORD = 'Ayushi14'
