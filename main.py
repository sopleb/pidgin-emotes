import os, json

os.remove('result.json')
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
