import requests as req, re

url_target = 'https://www.ivsky.com/tupian/haiyangshijie/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = req.get(url= url_target, headers= headers)
html     = response.text
urlArray = re.findall('<p><a href="(.*?)" title=".*?>" target="_blank">.*?</a></p>', html)

for url in urlArray:
    print(url)