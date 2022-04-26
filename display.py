from flask import Flask

"""显示用户头像"""
app = Flask(__name__)


@app.route("/display")
def haha():
    return "Hello"


if __name__ == '__main__':
    app.run()
