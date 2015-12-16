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

    @app.route('/event_add')
    def event_add():
        return render_template('event_add.html')

    ############
    # promises #
    ############
    @app.route('/promises')
    def promises():
        return render_template('promises.html')

    @app.route('/promise_add')
    def promise_add():
        return render_template('promise_add.html')

    #############
    # whishlist #
    #############
    @app.route('/whishlist')
    def whishlist():
        return render_template('whishlist.html')

    @app.route('/whishlist_add')
    def whishlist_add():
        return render_template('whishlist_add.html')

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

    @app.route('/category_add')
    def category_add():
        return render_template('category_add.html')

    #########
    # users #
    #########
    @app.route('/users')
    def users():
        return render_template('users.html')

    @app.route('/user_add')
    def user_add():
        return render_template('user_add.html')

    @app.route('/add_user', methods=['POST'])
    def add_user():
        user = request.get_json()

        db = mongo_instance.get_mongo_db()
        u = db.user.insert(user)

        return "{}".format(u)


