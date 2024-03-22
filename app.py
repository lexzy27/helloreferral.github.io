from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello():
    return render_template('hello.html')

    @app.route('/')
def hello_referral():
     return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
        