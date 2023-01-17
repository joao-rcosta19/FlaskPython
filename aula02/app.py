from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

def teste():
    return "<p> teste ok </p>"

def teste2():
    return "<h1> teste </h1>"

app.add_url_rule("/teste", "teste", teste)
app.add_url_rule("/teste-2", "teste2", teste2)


if __name__ == '__main__':
    app.run(debug=True, port="3000")