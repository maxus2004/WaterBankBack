from flask import Flask
from flask import request
import json

app = Flask(__name__)

bottles = {}

@app.route('/get')
def getcmd():
    location = request.args.get('id')
   
    return json.dumps({"count":bottles[location]})

@app.route('/set')
def setcmd():
    location = request.args.get('id')
    count = request.args.get('count')
    bottles[location] = count;
    return json.dumps({"result":"ok"})

@app.route('/add')
def addcmd():
    location = request.args.get('id')
    count = request.args.get('count')
    bottles[location] += count;
    return json.dumps({"result":"ok"})
    
@app.route('/remove')
def removecmd():
    location = request.args.get('id')
    count = request.args.get('count')
    if(bottles[location] >= count)
        bottles[location] -= count
        bottles[location])
        return json.dumps({"result":"ok"})
    else
    return json.dumps({"result":"not_enough_bottles"})
    
app.run(port=5000)