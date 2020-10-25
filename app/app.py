from flask import Flask
from src.domain.phone import Phone

app = Flask(__name__)


@app.route("/")
def hello():
    name: str = "Hello World"
    return name


@app.route("/good")
def good():
    name = "Good"
    return name


@app.route("/phone")
def phone():
    phone = Phone("iPhone 12")
    return phone.get_name()


## おまじない
if __name__ == "__main__":
    app.run(debug=True)
