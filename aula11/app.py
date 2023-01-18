from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder="templetes")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/setcookie", methods=["GET", "POST"])
def setcookie():
    resp = make_response(render_template("setcookie.html"))
    if request.method == "POST":
        dados = request.form["testCookie"]
        resp.set_cookie("testeCookie", dados)
    return resp

@app.route("/getcookie")
def getcookie():
    cookiename= request.cookies.get("testeCookie")
    return "<h1>Valor do Cookie é: {}</h1>".format(cookiename)

if __name__ == "__main__":
    app.run(debug=True)