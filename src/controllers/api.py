from flask_restplus import Resource
from flask import request


def initialize(ns, api, mongo_instance):

    def get_db():
        return mongo_instance.get_mongo_db()

    @ns.route('/events')
    class Events(Resource):

        def get(self):
            f = ()
            try:
                f = list(get_db().events.find({}, {'_id': False}))
            except Exception as ex:
                f = str(ex)
            return f

        def post(self):
            data = request.get_json()
            get_db().events.insert(data)
            return "data: {}".format(data)

    @ns.route('/promises')
    class Promises(Resource):

        def get(self):
            return list(get_db().promises.find({}, {'_id': False}))

        def post(self):
            data = request.get_json()
            get_db().promises.insert(data)
            return "data: {}".format(data)

    @ns.route('/whishlist')
    class Whishlist(Resource):

        def get(self):
            return list(get_db().whishlist.find({}, {'_id': False}))

        def post(self):
            data = request.get_json()
            get_db().whishlist.insert(data)
            return "data: {}".format(data)
