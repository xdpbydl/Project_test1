import json

info = {'name':'alex','age':22}

f = open('test.text','r')
data = json.loads(f.read())
print(data['age'])