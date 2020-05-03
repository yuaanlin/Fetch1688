# coding=utf-8

import requests
import settings as cfg

def item_serch(keyword, page):
    '''
    調用 Onebound API 的 item_search 接口
    '''
    
    print('正在獲取 {} 的商品清單，目前查看第 {} 頁 ...'.format(keyword, page))
    items = []
    url = "https://api.onebound.cn/1688/api_call.php?key={apiKey}&secret={apiSecret}&api_name=item_search&q={keyword}&page={page}".format(apiKey=cfg.api['key'], apiSecret=cfg.api['secret'], keyword=keyword, page=page)
    r = requests.get(url, headers=cfg.headers)
    json_obj = r.json()
    for item in json_obj['items']['item']:
        items.append(item)
    print('成功從 {} 商品清單的第 {} 頁 抓取 {} 筆數據'.format(keyword, page, len(items)))
    return items
    
def item_get(iid):
    '''
    調用 Onebound API 的 item_get 接口
    '''
    
    print('正在獲取編號 {} 的商品資訊 ...'.format(iid))
    url = "https://api.onebound.cn/1688/api_call.php?key={apiKey}&secret={apiSecret}&api_name=item_get&num_iid={iid}".format(apiKey=cfg.api['key'], apiSecret=cfg.api['secret'], iid=iid)
    r = requests.get(url, headers=cfg.headers)
    json_obj = r.json()['item']
    print('獲取到編號 {} 的商品資訊了: {}'.format(iid, json_obj['title']))
    return json_obj