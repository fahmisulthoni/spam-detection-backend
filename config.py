import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object) :

    #HOST = "localhost"
    #DATABASE = "twispad"
    #USERNAME = "postgres"
    #PASSWORD = "amisijenius303"

    #SQLALCHEMY_DATABASE_URI = 'postgresql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_DATABASE_URI = 'postgresql://tjhtebzrnrjmqk:95c1b3d1755316bdb5ccf8131d637dc90af2b956ff892922b270195843833b47@ec2-52-206-193-199.compute-1.amazonaws.com:5432/d22ng53fdvraor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True