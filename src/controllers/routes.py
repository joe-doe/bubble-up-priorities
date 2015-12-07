from flask import (
    render_template,
    request
)


def initialize(app, mongo_instance):
    @app.route('/')
    def hello():
        return render_template('index2.html')
        # return render_template('vertical_tabs.html')

    @app.route('/main')
    def main():
        return render_template('main.html')

    @app.route('/test')
    def test():
        return render_template('input.html')

    @app.route('/calendar')
    def calendar():
        return render_template('full_calendar.html')

    @app.route('/set_user', methods=['POST'])
    def set_user():
        user = request.get_json()

        db = mongo_instance.get_mongo_db()
        u = db.user.insert(user)

        return "{}".format(u)

    @app.route('/set_event', methods=['POST'])
    def set_event():
        name = request.form['name']
        password = request.form['password']

        db = mongo_instance.get_mongo_db()
        entry = {
            "name": name,
            "pass": password
        }

        u = db.user.insert(entry)
        print u
        return "{}".format(u)