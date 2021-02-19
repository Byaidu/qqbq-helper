import json
import os

db=[]
for id in range(194868,208944+1):
    if (id%1000==0):
        print(id)
    if os.path.exists(f'xydata\{id}.js'):
        with open(f'xydata\{id}.js','r',encoding='utf-8') as f:
            rawjs=f.read()
            rawjson=json.loads(rawjs[27:])
            info=rawjson['data']['baseInfo'][0]
            sliminfo={'id':id,'desc':info['desc'],'name':info['name'],'tag':info['tag']}
            db.append(sliminfo)
            #print(db)

with open(f'db.json','w',encoding='utf-8') as f:
    f.write(json.dumps(db,ensure_ascii=False))