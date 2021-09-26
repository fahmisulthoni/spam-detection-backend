import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object) :

    #HOST = "localhost"
    #DATABASE = "twispad"
    #USERNAME = "postgres"
    #PASSWORD = "amisijenius303"

    #SQLALCHEMY_DATABASE_URI = 'postgresql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_DATABASE_URI = 'postgresql://rbhrlraspwsegz:22e02ef18e5585c8bf7cb19b8e44f5303e10e6c68cb3b6bfb483eff97c5d8b6a@ec2-34-233-187-36.compute-1.amazonaws.com:5432/d7a92tefva6ubq'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True