from flask import Flask
from src.model.database import Database
from src.controllers import routes

app = Flask(__name__,
            template_folder='src/view/pages',
            static_folder='src/view/static')
app.secret_key = 'development key'


mongo_instance = Database()


routes.initialize(app, mongo_instance)


if __name__ == '__main__':
    app.run(threaded=True,
            debug=False,
            use_reloader=False,
            host='192.168.56.101',
            port=5001)
