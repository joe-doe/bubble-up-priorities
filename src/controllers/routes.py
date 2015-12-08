from flask import (
    render_template,
    request
)


def initialize(app, mongo_instance):

    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/main')
    def main():
        return render_template('main.html')

    ##########
    # events #
    ##########
    @app.route('/events')
    def events():
        return render_template('events.html')

    ############
    # promises #
    ############
    @app.route('/promises')
    def promises():
        return render_template('promises.html')

    #############
    # whishlist #
    #############
    @app.route('/whishlist')
    def whishlist():
        return render_template('whishlist.html')

    ############
    # calendar #
    ############
    @app.route('/calendar')
    def calendar():
        return render_template('calendar.html')

    ##############
    # categories #
    ##############
    @app.route('/categories')
    def categories():
        return render_template('categories.html')


    #########
    # users #
    #########
    @app.route('/users')
    def users():
        return render_template('users.html')

    @app.route('/add_user_form')
    def add_user_form():
        return render_template('add_user_form.html')

    @app.route('/add_user', methods=['POST'])
    def add_user():
        user = request.get_json()

        db = mongo_instance.get_mongo_db()
        u = db.user.insert(user)

        return "{}".format(u)
