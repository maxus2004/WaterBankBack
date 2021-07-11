def save(bottles):
    file = open('result.json', 'w')
    json.dump(file, bottles)
    file.close()
    
def load():
    file = open('result.json', 'r')
    bottles = json.loads(file.read())
    file.close()
    return bottles