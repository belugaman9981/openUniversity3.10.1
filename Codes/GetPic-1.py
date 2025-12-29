import requests as req


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


url = 'https://www.ivsky.com/tupian/haiyangshijie/'
response = req.get(url= url, headers= headers)
html     = response.text
print(html)
