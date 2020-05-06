# "Fetch1688" Python API 串接程式使用說明

## 目錄

-   ["Fetch1688" Python API 串接程式使用說明](#%22fetch1688%22-python-api-%e4%b8%b2%e6%8e%a5%e7%a8%8b%e5%bc%8f%e4%bd%bf%e7%94%a8%e8%aa%aa%e6%98%8e)
    -   [目錄](#%e7%9b%ae%e9%8c%84)
    -   [前置需求](#%e5%89%8d%e7%bd%ae%e9%9c%80%e6%b1%82)
        -   [Python 3](#python-3)
        -   [tqdm](#tqdm)
        -   [requests](#requests)
        -   [pymssql](#pymssql)
    -   [環境設定](#%e7%92%b0%e5%a2%83%e8%a8%ad%e5%ae%9a)
        -   [萬邦 API 金鑰](#%e8%90%ac%e9%82%a6-api-%e9%87%91%e9%91%b0)
        -   [資料庫連線參數](#%e8%b3%87%e6%96%99%e5%ba%ab%e9%80%a3%e7%b7%9a%e5%8f%83%e6%95%b8)
    -   [使用](#%e4%bd%bf%e7%94%a8)
        -   [第一階段](#%e7%ac%ac%e4%b8%80%e9%9a%8e%e6%ae%b5)
        -   [第二階段](#%e7%ac%ac%e4%ba%8c%e9%9a%8e%e6%ae%b5)
        -   [第三階段](#%e7%ac%ac%e4%b8%89%e9%9a%8e%e6%ae%b5)

## 前置需求

以下是執行該程式前需準備的前置需求，請確保所有需求皆符合後再執行程式。

### Python 3

本程式需要使用 Python3 來執行，請先確保您的執行環境已有可用的 Python3

透過該指令檢查您的 Python 版本

`python3 --version`

### tqdm

本程式需要安裝 Python 的 tqdm 套件，用於顯示下載進度的進度條。

**安裝該套件** `python3 -m pip install tqdm`

**檢查是否安裝完成** `python3 -m pip show tqdm`

看到以下內容代表安裝成功

```shell
Name: tqdm
Version: 4.46.0
Summary: Fast, Extensible Progress Meter
Home-page: https://github.com/tqdm/tqdm
Author: None
Author-email: None
License: MPLv2.0, MIT Licences
Location: /Users/yuanlin/Library/Python/3.7/lib/python/site-packages
Requires:
Required-by:
```

### requests

本程式需要安裝 Python 的 requests 套件，用於對 API 發出請求。

**安裝該套件** `python3 -m pip install requests`

**檢查是否安裝完成** `python3 -m pip show requests`

看到以下內容代表安裝成功

```shell
Name: requests
Version: 2.23.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: /Users/yuanlin/Development/fetch1688/env/lib/python3.7/site-packages
Requires: idna, certifi, urllib3, chardet
Required-by:
```

### pymssql

本程式需要安裝 Python 的 pymssql 套件，用於連線至 MSSQL 資料庫。

参見微軟提供的 [設定 pymssql Python 開發的開發環境](https://docs.microsoft.com/zh-tw/sql/connect/python/pymssql/step-1-configure-development-environment-for-pymssql-python-development?view=sql-server-ver15)

## 環境設定

在 `settings.py` 中，您需要手動設定以下參數。

#### 萬邦 API 金鑰

```python
# settings.py
api = {
    'url': 'https://api.onebound.cn/1688/api_call.php',
    'key': '您的 APIKey',
    'secret': '您的 APISecret'
}
```

#### 資料庫連線參數

```python
# settings.py
sql = {
    'host': '主機地址',
    'username': '用戶名',
    'password': '用戶密碼',
    'database': '資料庫名'
}
```

## 使用

程式的使用方法是 `python3 main.py <關鍵詞> <起始頁碼>`

### 第一階段

當您輸入這個命令以後，程式會進入第一階段，根據該 `關鍵詞` 從您設定的 `起始頁碼` 搜尋商品，

```shell
> python3 main.py

第一階段：搜尋商品
    程式將開始循環查詢關鍵字 「女裝」 並紀錄所有搜尋到的商品 id,
    當您覺得數量足夠後請使用 Ctrl + C 結束循環, 程式即可進入第二階段

目前已經搜尋到 60 個關於 「女裝」 的商品了 (按 Ctrl + C 進入第二階段）

目前已經搜尋到 120 個關於 「女裝」 的商品了 (按 Ctrl + C 進入第二階段）

目前已經搜尋到 180 個關於 「女裝」 的商品了 (按 Ctrl + C 進入第二階段）
```

當您覺得商品數量足夠以後，使用 `Ctrl + C` 結束第一階段。

### 第二階段

```shell
^C
第一階段程式執行完畢。
    總共搜尋到了 180 個商品

第二階段：下載商品
程式將根據剛剛搜尋到的商品 id, 下載其詳細資料並保存於本地。
下載完成後將自動開始第三階段。


商品下載進度: 100%|████████████| 180/180 [00:12<00:00, 14.33it/s]
```

在第二階段中，程式會根據第一階段獲取到的商品 id 清單，下載這些商品的詳細資料。

### 第三階段

下載完成後程式會自動進入第三階段。

```shell
第三階段：上傳至資料庫
程式將把下載好的商品資料上傳至資料庫。
```

第三階段中，程式會把下載到的詳細資料放入資料庫中。

```
程式執行完成，請查看資料庫的 data20200505 資料表。
```

當您看到本訊息，即可關閉程式並查看資料庫中新增的資料表。

> 資料表格式是根據萬邦 API 回傳的商品資料所建置，欄位說明請諮詢萬邦服務人員。
