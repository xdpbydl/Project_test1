import json
'''pickle'''

info = {'name':'alex','age':22}

f = open('test.text','w')
f.write(json.dumps(info))