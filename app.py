from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/get')
def getcmd():
    location = request.args.get('id')
    return json.dumps({"count":5})

@app.route('/set')
def setcmd():
    location = request.args.get('id')
    count = request.args.get('count')
    return json.dumps({"result":"ok"})

@app.route('/add')
def addcmd():
    location = request.args.get('id')
    count = request.args.get('count')
    return json.dumps({"result":"ok"})
    
@app.route('/remove')
def removecmd():
    location = request.args.get('id')
    count = request.args.get('count')
    return json.dumps({"result":"ok"})
    
    
app.run(port=5000)