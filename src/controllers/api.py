from flask_restplus import Resource
from flask import request
from bson.objectid import ObjectId

def initialize(ns, api, mongo_instance):

    def get_db():
        return mongo_instance.get_mongo_db()

    @ns.route('/events/<action>')
    class Events(Resource):

        def get(self, action):
            if action == 'get':
                events = []
                records = list(get_db().events.find({}))
                for record in records:
                    event = record
                    event['id'] = str(record['_id'])
                    del(event['_id'])
                    events.append(event)
                return events
                # return list(get_db().events.find({}, {'_id': False}))
            else:
                return {"status": "invalid action"}

        def post(self, action):

            return_value = {"status": "OK"}

            if action == 'add':
                data = request.get_json()
                get_db().events.insert(data)
            elif action == 'delete':
                data = request.get_json()
                ev = get_db().events.find(data)
                print ev
            elif action == 'update':
                data = request.get_json()
                object_id = ObjectId(data['_id'])
                data['_id'] = object_id
                get_db().events.update({'_id': object_id}, data)
            else:
                return_value = {"status": "invalid action"}

            return "data: {}".format(return_value)

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
