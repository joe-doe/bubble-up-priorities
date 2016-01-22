from flask import Flask
from flask_restplus import Api
import os.path

from src.model.database import Database
from src.controllers import (
    routes,
    api
)

app = Flask(__name__,
            template_folder='src/view/pages',
            static_folder='src/view/static')

config_module = 'local_config' if os.path.isfile('local_config.py') else 'config'
app.config.from_object(config_module)

restplus_api = Api(app,
                   version='1.0',
                   title='bubup !'
                   )
ns = restplus_api.namespace(name='api', description='WOW bubup !')
mongo_instance = Database(app)

api.initialize(ns, restplus_api, mongo_instance)
routes.initialize(app, mongo_instance)

if __name__ == '__main__':
    # for x in app.url_map.iter_rules():
    #     print x

    app.run(threaded=True,
            debug=True,
            use_reloader=False,
            host='192.168.56.101',
            port=5001)
