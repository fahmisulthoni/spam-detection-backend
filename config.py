import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object) :

    #HOST = "localhost"
    #DATABASE = "twispad"
    #USERNAME = "postgres"
    #PASSWORD = "amisijenius303"

    #SQLALCHEMY_DATABASE_URI = 'postgresql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_DATABASE_URI = 'postgresql://usjlxebtamfiwz:c1d95733083830acc28e052ab29355bd14d78614bfef9444576242862aeefd13@ec2-18-209-143-227.compute-1.amazonaws.com:5432/dd0eeb7v99m4en'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True