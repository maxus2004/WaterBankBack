from flask import Flask
from flask import request
import json
import tools

app = Flask(__name__)

bottles = tools.load()

@app.route('/create')
def createcmd():
    if not check(request.cookies.get('key')):
        return json.dumps({"result":"not_authorised"})
    
    location = request.args.get('id')
    public = request.args.get('public')=='true'
    bottles[location] = {'count':0,'public':public};
    tools.save(bottles)
    return json.dumps({"result":"ok"})

@app.route('/getall')
def getallcmd():
    if not check(request.cookies.get('key')):
        return json.dumps({"result":"not_authorised"})
    
    return json.dumps(bottles)

@app.route('/get')
def getcmd():
    if not check(request.cookies.get('key')):
        return json.dumps({"result":"not_authorised"})

    location = request.args.get('id')
    return json.dumps(bottles[location])
    
@app.route('/getpublic')
def getpubliccmd():
    array = {}
    for id in bottles:
        if bottles[id]['public']:
            array[id]=bottles[id]
    return json.dumps(array)

@app.route('/set')
def setcmd():
    if not check(request.cookies.get('key')):
        return json.dumps({"result":"not_authorised"})
    
    location = request.args.get('id')
    count = int(request.args.get('count'))
    bottles[location]['count'] = count
    tools.save(bottles)
    return json.dumps({"result":"ok"})

@app.route('/add')
def addcmd():
    if not check(request.cookies.get('key')):
        return json.dumps({"result":"not_authorised"})
    
    location = request.args.get('id')
    count = int(request.args.get('count'))
    bottles[location]['count'] += count
    tools.save(bottles)
    return json.dumps({"result":"ok"})
    
@app.route('/remove')
def removecmd():
    if not check(request.cookies.get('key')):
        return json.dumps({"result":"not_authorised"})
    
    location = request.args.get('id')
    count = int(request.args.get('count'))
    if bottles[location]['count'] >= count:
        bottles[location]['count'] -= count
        tools.save(bottles)
        return json.dumps({"result":"ok"})
    else:
        return json.dumps({"result":"not_enough_bottles"})
        
@app.route('/move')
def movecmd():
    if not check(request.cookies.get('key')):
        return json.dumps({"result":"not_authorised"})
    
    fromId = request.args.get('from')
    toId = request.args.get('to')
    count = int(request.args.get('count'))
    if bottles[fromId]['count'] >= count:
        bottles[fromId]['count'] -= count
        bottles[toId]['count'] += count
        tools.save(bottles)
        return json.dumps({"result":"ok"})
    else:
        return json.dumps({"result":"not_enough_bottles"})
   
   
   
app.run(port=5000)