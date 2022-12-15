import os, json

try:
    os.remove('result.json')
except FileNotFoundError as e:
    pass
emotepath = os.listdir('gsf')
emotepath.sort()
noext = [x.split('.')[0] for x in emotepath]
rlist = []

for i in noext:
    key = str(":"+i+":")
    rlist.append(key)

result=dict(zip(rlist, emotepath))

with open('result.json', 'w') as f:
    json.dump(result, f,)
