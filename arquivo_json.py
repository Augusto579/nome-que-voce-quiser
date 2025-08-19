import json

with open('seuarquivo.json', newline='', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)
    print(data)