from flask import Flask
from src.domain.phone import Phone

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    name: str = "Hello World"
    return name


@app.route("/good")
def good() -> str:
    name = "Good"
    return name


@app.route("/phone")
def phone() -> str:
    phone = Phone("iPhone 12")
    return phone.get_name()


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
