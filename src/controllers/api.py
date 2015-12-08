from flask_restplus import Resource
from flask import request
from bson.json_util import dumps


def initialize(ns, api, mongo_instance):

    @ns.route('/events')
    class Events(Resource):

        def get_db(self):
            return mongo_instance.get_mongo_db()

        def get(self):
            return dumps(self.get_db().events.find({}, {'_id': False}))

        def post(self):
            data = request.get_json()
            self.get_db().events.insert(data)
            return "data: {}".format(data)
