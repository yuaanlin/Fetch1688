# coding=utf-8

import pymssql
import settings as cfg

from datetime import datetime

def upload_items(items):
    conn = pymssql.connect(server=cfg.sql['host'], user=cfg.sql['username'], password=cfg.sql['password'], database=cfg.sql['database'])
    cursor = conn.cursor()
    
    # 新建、插入操作
    cursor.execute("""
    IF OBJECT_ID('data{today}', 'U') IS NOT NULL
    DROP TABLE data{today}
    CREATE TABLE data{today} (
    num_iid nvarchar(100) NOT NULL,
    title nvarchar(100),
    detail_url nvarchar(400),
    origin_data nvarchar(max),
    PRIMARY KEY(num_iid)
    )
    """.format(today=datetime.now().strftime("%Y%m%d")))
    
    datas = []
    for item in items:
        datas.append((str(item['num_iid']), str(item['title']), str(item['detail_url']), str(item)))

    cursor.executemany("INSERT INTO data{today} VALUES (%s, %s, %s, %s)".format(today=datetime.now().strftime("%Y%m%d")), datas)
    
    conn.commit()
    conn.close()