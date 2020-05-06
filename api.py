# coding=utf-8

import json

import requests

import settings as cfg
from langconv import Converter


def item_serch(keyword, page):
    '''
    調用 Onebound API 的 item_search 接口，回傳商品資料陣列
    '''
    
    items = []
    url = "{url}?key={apiKey}&secret={apiSecret}&api_name=item_search&q={keyword}&page={page}".format(url=cfg.api['url'], apiKey=cfg.api['key'], apiSecret=cfg.api['secret'], keyword=keyword, page=page)
    
    try:
        r = requests.get(url, headers=cfg.headers)
        json_obj = r.json()
    except Exception as e:
        print('''解析 API 回傳的資料時發生未預期的錯誤，可能是 API 沒有正常運作造成的。''')
        print('錯誤信息：')
        print(e)
        print('')
        exit()
    
    # API 例外處理
    if 'items' not in json_obj:
        print('''API 服務發生錯誤。''')
        if 'error' in json_obj:
            print('錯誤信息：')
            print(json_obj['error'])
            print('')
        exit()
        
    for item in json_obj['items']['item']:
        items.append(item)
    
    return items
    
def item_get(iid):
    '''
    調用 Onebound API 的 item_get 接口，回傳商品詳細數據
    '''
    
    url = "{url}?key={apiKey}&secret={apiSecret}&api_name=item_get&num_iid={iid}".format(url=cfg.api['url'], apiKey=cfg.api['key'], apiSecret=cfg.api['secret'], iid=iid)
    
    downloaded = False
    
    while not downloaded:
        try:
            r = requests.get(url, headers=cfg.headers).json()
            r_t = Converter('zh-hant').convert(json.dumps(r, ensure_ascii=False))
            json_obj = json.loads(r_t)
        except Exception as e:
            print('''解析 API 回傳的資料時發生未預期的錯誤，可能是 API 沒有正常運作造成的。''')
            print('錯誤信息：')
            print(e)
            print('')
            exit()
        
        # API 例外處理
        if 'item' not in json_obj:
            print('''API 服務發生錯誤，請聯繫 API 供應商或程式開發者。''')
            if 'error' in json_obj:
                print('錯誤信息：')
                print(json_obj['error'])
                print('')
            exit()
        
        item = json_obj['item']
        
        # 如果下載的資料不是空白的才結束循環
        if item['title'] != '':
            downloaded = True
    
    return item
