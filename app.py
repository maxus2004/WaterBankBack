from flask import Flask
from flask import request
import json
import tools

app = Flask(__name__)

bottles = tools.load()

@app.route('/create')
def createcmd():
    location = request.args.get('id')
    public = bool(request.args.get('public'))
    bottles[location] = {'count':0,'public':public};
    tools.save(bottles)
    return json.dumps({"result":"ok"})

@app.route('/getall')
def getallcmd():
    return json.dumps(bottles)

@app.route('/get')
def getcmd():
    location = request.args.get('id')
    return json.dumps({"count":bottles[location]})

@app.route('/set')
def setcmd():
    location = request.args.get('id')
    count = int(request.args.get('count'))
    bottles[location].count = count
    tools.save(bottles)
    return json.dumps({"result":"ok"})

@app.route('/add')
def addcmd():
    location = request.args.get('id')
    count = int(request.args.get('count'))
    bottles[location].count += count
    tools.save(bottles)
    return json.dumps({"result":"ok"})
    
@app.route('/remove')
def removecmd():
    location = request.args.get('id')
    count = int(request.args.get('count'))
    if bottles[location].count >= count:
        bottles[location].count -= count
        tools.save(bottles)
        return json.dumps({"result":"ok"})
    else:
        return json.dumps({"result":"not_enough_bottles"})
        
@app.route('/move')
def movecmd():
    fromId = request.args.get('from')
    toId = request.args.get('to')
    count = int(request.args.get('count'))
    if bottles[fromId].count >= count:
        bottles[fromId].count -= count
        bottles[toId].count += count
        tools.save(bottles)
        return json.dumps({"result":"ok"})
    else:
        return json.dumps({"result":"not_enough_bottles"})
    
app.run(port=5000)