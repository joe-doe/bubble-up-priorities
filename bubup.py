from flask import Flask, render_template

app = Flask(__name__,
            template_folder='src/view/pages',
            static_folder='src/view/static')


@app.route('/')
def hello():
    return render_template('vertical_tabs.html')


if __name__ == '__main__':
    app.run(threaded=True,
            debug=False,
            use_reloader=False,
            host='0.0.0.0',
            port=5001)
