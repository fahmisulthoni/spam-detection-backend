import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object) :

    #HOST = "localhost"
    #DATABASE = "twispad"
    #USERNAME = "postgres"
    #PASSWORD = "amisijenius303"

    #SQLALCHEMY_DATABASE_URI = 'postgresql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_DATABASE_URI = 'postgresql://dpklknarnehyzd:d04c92f1c6356b83edfd56abcf6526be787b7b4dbd44160a82aa3a1b60a57078@ec2-54-145-110-118.compute-1.amazonaws.com:5432/dcjhounp5d7bec'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True