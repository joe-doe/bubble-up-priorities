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
            self.mongo_client = MongoClient('mongodb://db_user:db_user1@ds027345.mongolab.com:'
                                            '27345/heroku_mongodb?authMode=scram-sha1')
            self.mongo_db = self.mongo_client.heroku_mongodb

            #self.mongo_client = MongoClient('mongodb://localhost:27017/')
            #self.mongo_db = self.mongo_client.mydb

            print "Connected successfully!!!"
        except errors.ConnectionFailure, e:
            print "Could not connect to MongoDB: %s" % e

    def get_client(self):
        return self.mongo_client

    def get_mongo_db(self):
        return self.mongo_db
