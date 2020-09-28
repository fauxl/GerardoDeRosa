import  flask
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("Index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)