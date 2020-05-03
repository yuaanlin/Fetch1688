# coding=utf-8

from multiprocessing import Pool 
from api import item_serch, item_get
from db import upload_items

def main():
    
    # 下載一個頁面內的商品
    items = item_serch('女装', 1)
    
    # 抽出該頁面商品的 id
    item_ids = []
    for item in items:
        if len(item_ids) < 5:
            item_ids.append(item['num_iid'])
    
    # 多進程下載該頁面商品的詳細資料
    pool = Pool()
    item_datas = pool.map(item_get, item_ids)
    
    upload_items(item_datas)
        
if __name__ == "__main__":
    main()