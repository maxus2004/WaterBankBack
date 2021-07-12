from flask import Flask
from flask import request
import json
import tools

app = Flask(__name__)

bottles = tools.load()

ok = json.dumps({"status":"ok"})
unauth = json.dumps({"status":"unauthorised"})
notenouth = json.dumps({"status":"not_enough_bottles"})

@app.route('/login')
def logincmd():
    password = request.args.get('pass')
    if not tools.checkPass():
        return unaut
    key = tools.makeKey()
    resp = app.make_response(json.dumps({"key":key}))
    resp.set_cookie('key', key)
    return resp

@app.route('/create')
def createcmd():
    if not tools.check(request.cookies.get('key')):
        return unauth
    location = request.args.get('id')
    public = request.args.get('public')=='true'
    bottles[location] = {'count':0,'public':public};
    tools.save(bottles)
    return ok

@app.route('/getall')
def getallcmd():
    if not tools.check(request.cookies.get('key')):
        return unauth
    return json.dumps(bottles)

@app.route('/get')
def getcmd():
    if not tools.check(request.cookies.get('key')):
        return unauth
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
    if not tools.check(request.cookies.get('key')):
        return unauth
    location = request.args.get('id')
    count = int(request.args.get('count'))
    bottles[location]['count'] = count
    tools.save(bottles)
    return ok

@app.route('/add')
def addcmd():
    if not tools.check(request.cookies.get('key')):
        return unauth
    location = request.args.get('id')
    count = int(request.args.get('count'))
    bottles[location]['count'] += count
    tools.save(bottles)
    return ok
    
@app.route('/remove')
def removecmd():
    if not tools.check(request.cookies.get('key')):
        return unauth
    location = request.args.get('id')
    count = int(request.args.get('count'))
    if bottles[location]['count'] >= count:
        bottles[location]['count'] -= count
        tools.save(bottles)
        return ok
    else:
        return notenouth
        
@app.route('/move')
def movecmd():
    if not tools.check(request.cookies.get('key')):
        return unauth
    fromId = request.args.get('from')
    toId = request.args.get('to')
    count = int(request.args.get('count'))
    if bottles[fromId]['count'] >= count:
        bottles[fromId]['count'] -= count
        bottles[toId]['count'] += count
        tools.save(bottles)
        return ok
    else:
        return notenouth
   
   
app.run(port=5000)