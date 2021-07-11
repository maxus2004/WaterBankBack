from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/get')
def index():
    location = request.args.get('id')
    return 'hello ' + location
    
app.run(port=5000)