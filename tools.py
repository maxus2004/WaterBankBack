import os
import json
import random
import string

keys = []

def save(bottles):
    file = open('bottles.json', 'w')
    json.dump(bottles, file)
    file.close()
    
def load():
    if os.path.exists('bottles.json'):
        file = open('bottles.json', 'r')
        bottles = json.load(file)
        file.close()
        return bottles
    else:
        return {}
        
def check(key):
    return key in keys
    
def makeKey():
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
    keys.append(key)
    return key