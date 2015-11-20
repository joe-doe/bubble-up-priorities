from flask import Flask, render_template

app = Flask(__name__,
            template_folder='src/view/pages',
            static_folder='src/view/static')


@app.route('/')
def hello():
    return render_template('index.html')
    # return render_template('vertical_tabs.html')


@app.route('/calendar')
def calendar():
    return render_template('full_calendar.html')


if __name__ == '__main__':
    app.run(threaded=True,
            debug=False,
            use_reloader=False,
            host='192.168.56.101',
            port=5001)
