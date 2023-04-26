import requests

url = 'https://apis.jxcxin.cn/api/mi?user=zhuanfa0@qq.com&password=a12345678&step=30000'
response = requests.get(url)
html = response.text
print(html)
