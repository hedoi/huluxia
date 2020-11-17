import requests
import json
import time

'''
引入json
'''


def loadJson(jsonPath):
    with open(jsonPath, encoding='utf-8') as f:
        jD = json.load(f)
    return jD


huluxiaJson = loadJson("huluxia.json")
for hlx in huluxiaJson:
    def hlxStart():
        cat_id = hlx["cat_id"]
        data = dict(hlx["data"], **cat_id)
        res = requests.post(url=hlx["url"], headers=hlx["headers"], data=data)
        hlx["cat_id"]["cat_id"] += 1
        print(hlx["cat_id"]["cat_id"], res)
        if hlx["cat_id"]["cat_id"] == 40:
            time.sleep(5)
            hlxStart()
        elif hlx["cat_id"]["cat_id"] == 80:
            time.sleep(5)
            hlxStart()
        elif hlx["cat_id"]["cat_id"] == 111:
            return
        else:
            hlxStart()


hlxStart()