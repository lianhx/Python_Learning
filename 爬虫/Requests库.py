import requests

# head()方法
r = requests.head('http://httpbin.org/get')
print(r.headers)

# 向url POST一个字典，自动编码为form(表单)
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

# 向url POST一个字符串，自动编码为data
r = requests.post('http://httpbin.org/post', data='ABC')
print(r.text)

# put()方法，会将原有数据覆盖掉
r = requests.put('http://httpbin.org/put', data=payload)
print(r.text)
