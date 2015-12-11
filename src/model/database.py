from pymongo import (
    MongoClient,
    errors
)


class Database(object):

    mongo_client = None
    mongo_db = None

    def __init__(self):
        # Connection to Mongo DB
        try:
            self.mongo_client = MongoClient('mongodb://db_user:db_user1@ds029595.mongolab.com:29595/heroku-mongod?authMode=scram-sha1')
            # self.mongo_client = MongoClient('mongodb://localhost:27017/')
            self.mongo_db = self.mongo_client.heroku-mongod
            print "Connected successfully!!!"
        except errors.ConnectionFailure, e:
            print "Could not connect to MongoDB: %s" % e

    def get_client(self):
        return self.mongo_client

    def get_mongo_db(self):
        return self.mongo_db
