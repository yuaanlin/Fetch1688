# coding=utf-8

import sys
from datetime import datetime
from functools import partial
from multiprocessing import Pool

import tqdm

import settings as cfg
from api import item_get, item_serch
from bcolors import bcolors
from db import upload_items


def main(keyword, startPage):
    
    item_ids = []
    item_datas = []
    
    # *------- 第一階段 -------*
    try:
        
        print(bcolors.HEADER + '''
第一階段：搜尋商品
    程式將開始循環查詢關鍵字 「{}」 並紀錄所有搜尋到的商品 id, 
    當您覺得數量足夠後請使用 Ctrl + C 結束循環, 程式即可進入第二階段
'''.format(keyword) + bcolors.ENDC)

        curr_page = startPage

        while True:
            
            # 下載一個頁面內的商品
            items = item_serch(keyword, curr_page)

            # 抽出該頁面商品的 id
            for item in items:
                item_ids.append(item['num_iid'])
                    
            print('''目前已經搜尋到 {} 個關於 「{}」 的商品了 (按 Ctrl + C 進入第二階段）
    '''.format(len(item_ids), keyword))
                    
            # 下一頁
            curr_page += 1
            
    except KeyboardInterrupt:
        print(bcolors.OKGREEN + '''
第一階段程式執行完畢。
    總共搜尋到了 {} 個商品'''.format(len(item_ids)) + bcolors.ENDC)

    # *------- 第二階段 -------*
    print(bcolors.HEADER + '''
第二階段：下載商品
程式將根據剛剛搜尋到的商品 id, 下載其詳細資料並保存於本地。
下載完成後將自動開始第三階段。

''' + bcolors.ENDC)

    pool = Pool()
    for item in tqdm.tqdm(pool.imap_unordered(item_get, item_ids), total=len(item_ids), desc='商品下載進度'):
        item_datas.append(item)
        pass
    pool.close()
    pool.join()
   
   # *------- 第三階段 -------*
    print(bcolors.HEADER + '''
第三階段：上傳至資料庫
程式將把下載好的商品資料上傳至資料庫。''' + bcolors.ENDC)

    upload_items(item_datas)

    # *------- 結束 -------*
    print(bcolors.OKGREEN + '程式執行完成，請查看資料庫中的 Items 資料表。' + bcolors.ENDC)
        
if __name__ == "__main__":
    
    # 輸入參數錯誤的例外處理
    if len(sys.argv) < 3 or not sys.argv[2].isdigit():
        print(bcolors.FAIL + 
            '''請輸入 「商品關鍵字」 以及 「起始頁碼」
例如: python3 main.py 女裝 20''' + bcolors.ENDC
        )
        exit()
        
    # 沒有設定 API 參數的例外處理
    elif cfg.api['key'] == '' or cfg.api['secret'] == '' or cfg.api['url'] == '':
        print(bcolors.FAIL +  '請先在 settings.py 完整設定您的 API 參數' + bcolors.ENDC)
        exit()
        
    # 沒有設定 Database 參數的例外處理
    elif cfg.sql['host'] == '' or cfg.sql['username'] == '' or cfg.sql['password'] == '' or cfg.sql['database'] == '':
        print(bcolors.FAIL + '請先在 settings.py 完整設定您的 Database 參數' + bcolors.ENDC)
        exit()
    
    else:
        main(sys.argv[1], int(sys.argv[2]))
