from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/get')
def getcmd():
    location = request.args.get('id')
    return 'n bottles in ' + location

@app.route('/set')
def setcmd():
    location = request.args.get('id')
    count = request.args.get('count')
    return 'set bottles in ' + location + ' to ' + count
    
@app.route('/add')
def addcmd():
    location = request.args.get('id')
    count = request.args.get('count')
    return 'added ' + count + ' bottles to ' + location
    
@app.route('/remove')
def removecmd():
    location = request.args.get('id')
    count = request.args.get('count')
    return 'removed ' + count + ' bottles from ' + location
    
    
app.run(port=5000)