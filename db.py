# coding=utf-8

from datetime import datetime

import pymssql

import settings as cfg
from api import item_get
from bcolors import bcolors


def upload_items(items, dbname):
    '''
    把陣列中的 item 資料逐項上傳到資料庫
    '''
    
    # 連線到資料庫
    try:
        conn = pymssql.connect(server=cfg.sql['host'], user=cfg.sql['username'], password=cfg.sql['password'], database=cfg.sql['database'], login_timeout=cfg.sql['login_timeout'])
    except Exception as e:
        print(bcolors.FAIL + '''
連線至資料庫失敗:
        ''' + bcolors.ENDC)
        print(e)
        exit()
    
    try:
        cursor = conn.cursor()
        
        # 建表
        cursor.execute("""
        IF OBJECT_ID('{dbname}', 'U') IS NULL
        CREATE TABLE {dbname} (
        num_iid nvarchar(100) NOT NULL, title nvarchar(max), desc_short nvarchar(max), price nvarchar(max), total_price nvarchar(max), suggestive_price nvarchar(max), orginal_price nvarchar(max), nick nvarchar(max), num nvarchar(max), min_num nvarchar(max), detail_url nvarchar(max), pic_url nvarchar(max), brand nvarchar(max), brandId nvarchar(max), rootCatId nvarchar(max), cid nvarchar(max), favcount nvarchar(max), fanscount nvarchar(max), crumbs nvarchar(max), created_time nvarchar(max), modified_time nvarchar(max), delist_time nvarchar(max),
        description nvarchar(max), item_imgs nvarchar(max), item_weight nvarchar(max), item_size nvarchar(max), location nvarchar(max), post_fee nvarchar(max), express_fee nvarchar(max), ems_fee nvarchar(max), shipping_to nvarchar(max), has_discount nvarchar(max), video nvarchar(max), is_virtual nvarchar(max), sample_id nvarchar(max), is_promotion nvarchar(max), props_name nvarchar(max), prop_imgs nvarchar(max), property_alias nvarchar(max), props nvarchar(max), total_sold nvarchar(max), skus nvarchar(max), seller_id nvarchar(max), sales nvarchar(max), shop_id nvarchar(max), props_list nvarchar(max), seller_info nvarchar(max), tmall nvarchar(max), warning nvarchar(max), url_log nvarchar(max), priceRange nvarchar(max), sales_info nvarchar(max), origin_data nvarchar(max),
        PRIMARY KEY(num_iid)
        )
        """.format(dbname=dbname))
    except Exception as e:
        print(bcolors.FAIL + '''
資料庫操作時發生錯誤:
        ''' + bcolors.ENDC)
        print(e)
        exit()
    
    # 把資料整理成要上傳的格式
    added_ids = []
    datas = []
    for item in items:
        try:
            if item['num_iid'] not in added_ids:
                added_ids.append(item['num_iid'])
                datas.append((str(item['num_iid']), str(item['title']), str(item['desc_short']), str(item['price']), str(item['total_price']), str(item['suggestive_price']), str(item['orginal_price']), str(item['nick']), str(item['num']), str(item['min_num']), str(item['detail_url']), str(item['pic_url']), str(item['brand']), str(item['brandId']), str(item['rootCatId']), str(item['cid']), str(item['favcount']), str(item['fanscount']), str(item['crumbs']), str(item['created_time']), str(item['modified_time']), str(item['delist_time']), str(item['desc']), str(item['item_imgs']), str(item['item_weight']), str(item['item_size']), str(item['location']), str(item['post_fee']), str(item['express_fee']), str(item['ems_fee']), str(item['shipping_to']), str(item['has_discount']), str(item['video']), str(item['is_virtual']), str(item['sample_id']), str(item['is_promotion']), str(item['props_name']), str(item['prop_imgs']), str(item['property_alias']), str(item['props']), str(item['total_sold']), str(item['skus']), str(item['seller_id']), str(item['sales']), str(item['shop_id']), str(item['props_list']), str(item['seller_info']), str(item['tmall']), str(item['warning']), str(item['url_log']), str(item['priceRange']), str(item['sales_info']), str(item)))
        except Exception as e:
            print('')
            print(bcolors.FAIL + '上傳物品編號 {} 時發生了錯誤，因為收到的資料不符合格式 (缺少 {} 屬性)，因此他將被略。'.format(item['num_iid'], e) + bcolors.ENDC)
            
    
    try:
        
        # 清除重複的資料
        cursor.executemany('DELETE FROM {dbname} WHERE num_iid = %s'.format(dbname=dbname), added_ids)
        
        # 上傳所有資料
        cursor.executemany('INSERT INTO {dbname} VALUES (%s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)'.format(dbname=dbname), datas)
        
        conn.commit()
    except Exception as e:
        print(bcolors.FAIL + '''
資料庫操作時發生錯誤:
        ''' + bcolors.ENDC)
        print(e)
        exit()
        
    conn.close()
