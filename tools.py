def save(bottles):
    file = open('result.json', 'w')
    json.dump(bottles, file)
    file.close()
    
def load():
    file = open('result.json', 'r')
    bottles = json.load(file)
    file.close()
    return bottles