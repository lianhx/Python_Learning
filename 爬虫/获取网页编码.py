import requests

r = requests.get("http://www.bilibili.com")
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)  # 根据网页内容分析编码方式
r.encoding = 'utf-8'
# print(r.text)
