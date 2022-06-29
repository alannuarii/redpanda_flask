import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'redpanda.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = 'app/static/upload'
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024

  



