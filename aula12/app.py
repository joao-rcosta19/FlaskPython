from flask import Flask, session, render_template

app = Flask(__name__, template_folder='templetes')
app.secret_key = '123456'


if __name__ == "__main__":
    app.run(debug=True)