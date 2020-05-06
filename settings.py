# coding=utf-8

# API 請求 Headers (參照 Onebound 說明)
headers = {
    "Accept-Encoding": "gzip",
    "Connection": "close"
}

# API 服務授權參數
api = {
    'url': 'https://api.onebound.cn/1688/api_call.php',
    'key': '',
    'secret': '',
    
    # 請求 API 的超時限制
    'timeout': 10,
    
    # 重新下載商品資料的次數限制
    'max_try_times': 10
}

# 資料庫連線參數
sql = {
    'host': '',
    'username': '',
    'password': '',
    'database': '',
    
    # 嘗試連接資料庫的限制時間 (秒)
    'login_timeout': 10
}
