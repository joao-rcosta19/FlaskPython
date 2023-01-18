from flask import Flask, request
import json 

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    #print(request.method, request.args)
    ti = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps([ti['idade'], t2['nome']]) 
    #json.dumps([ti, t2])   
    #json.dumps(request.args)

if __name__ == "__main__":
    app.run(debug=True)