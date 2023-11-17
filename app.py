## Flask App Routing

from flask import Flask

## create a simple flask application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Welcome to my Flask page"

@app.route("/index",methods=["GET"])
def index():
    return "Welcome to the Index page"


if __name__ == "__main__":
    app.run(debug=True)


