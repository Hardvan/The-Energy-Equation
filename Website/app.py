# cd to the folder where the app.py file is located
# run the command: python app.py

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/ev')
def ev():

    return render_template("ev.html")


if __name__ == "__main__":
    app.run(debug=True)
