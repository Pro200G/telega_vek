import json

ar = []

with open('cens.txt', encoding='UTF-8') as r:
    for i in r:
        a = i.split('\n')[0]
        if i != '':
            ar.append(a)

with open('cenz.json', 'w', encoding='UTF-8') as c:
    json.dump(ar, c)