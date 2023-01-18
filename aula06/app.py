from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder="public")

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        return dumps(request.form)
        #return "ok POST result: %s." % request.form['nome']
    return "ok GET"

if __name__ == "__main__":
    app.run(debug=True)