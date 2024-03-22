from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route('/display')
def display():
 return render_template('display.html')


if __name__ == '__main__':
    app.run(debug=True)
    