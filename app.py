from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_referral():
    return "hello_referral!"
if __name__ == '__main__':
    app.run(debug=True)
    