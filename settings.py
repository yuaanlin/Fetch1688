# coding=utf-8

# API 請求 Headers (參照 Onebound 說明)
headers = {
    "Accept-Encoding": "gzip",
    "Connection": "close"
}

# API 服務授權參數
api = {
    'url': 'https://api.onebound.cn/1688/api_call.php',
    'key': 'tel886939015945',
    'secret': '20200503',
    
    # 請求 API 的超時限制
    'timeout': 10
}

# 資料庫連線參數
sql = {
    'host': 'localhost',
    'username': 'AbolrousHazem',
    'password': '340$Uuxwp7Mcxo7Khy',
    'database': 'master',
    
    # 嘗試連接資料庫的限制時間 (秒)
    'login_timeout': 10
}
