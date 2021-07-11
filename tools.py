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