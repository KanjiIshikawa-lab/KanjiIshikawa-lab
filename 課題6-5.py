# -*- coding: utf-8 -*-
 
import requests
import pandas as pd
# テスト対象の関数
import pytest

def pytestexam(x):
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20140222'
    payload = {
        'applicationId': 1017762098426453356,
        'keyword': 'Python',
        'hits': 10,
        'sort': '-itemPrice',
        "rankTargetProductCount":30485
    }
    r = requests.get(url, params=payload)
    resp = r.json()
    a=[]
    b=[]
    for i in resp['Items']:
        item = i['Item']
        a.append(item['itemName'])
        b.append(item['itemPrice'])
     #df = pd.DataFrame({"Items":a,"Prices":b})
     #df.to_csv("/Users/ishikawakanji/Desktop/課題6/item.csv", encoding="utf-8-sig")
    y = len(a) + x
    return y


def test():
    res = pytestexam(3)
    assert res == 13


if __name__ == "__main__":
    pytestexam(3)