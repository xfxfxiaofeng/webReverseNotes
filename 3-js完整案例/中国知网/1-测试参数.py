import requests
import json


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    # "ClientID": "__20bShh__R6UY2SqTJBqxsB8lUsTydm0UtEGzTt5e",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://kns.cnki.net",
    "Referer": "https://kns.cnki.net/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "appID": "LoginWap",
    # "nonce": "66338634816",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    # "signature": "5c844e3c25058c50e03dd3d428f82566",
    # "timestamp": "1754578367000"
}

url = "https://login.cnki.net/TopLoginCore/api/loginapi/LoginPo"
data = {
    "userName": "18888889888",
    "pwd": "h87jHL/jCApta+edah5s4w==",
    "isAutoLogin": True,
    "p": 0,
    "isEncry": 1
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(
    url, 
    headers=headers, 
    data=data
)

print(response.text)
print(response)