from pymongo import (
    MongoClient,
    errors
)

class Database(object):

    mongo_client = None
    mongo_db = None

    def __init__(self, app):
        # Connection to Mongo DB
        try:
            self.mongo_client = MongoClient(app.config.get('MONGODB_URI'))
            self.mongo_db = self.mongo_client.heroku_mongodb

            print "Connected successfully!!!"
        except errors.ConnectionFailure, e:
            print "Could not connect to MongoDB: %s" % e

    def get_client(self):
        return self.mongo_client

    def get_mongo_db(self):
        return self.mongo_db
