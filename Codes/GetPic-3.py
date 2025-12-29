import requests as req, re, os


url_target = 'https://www.ivsky.com/tupian/haiyangshijie/'
url_server = 'https://www.ivsky.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = req.get(url= url_target, headers= headers)
html     = response.text
urlArray = re.findall('<p><a href="(.*?)" title=".*?>" target="_blank">.*?</a></p>', html)

for url in urlArray:
    #三级域名
    pic_url = url_server + url #规范的可访问的地址
    print(pic_url)
    
    resp = req.get(url= pic_url, headers= headers)
    html_pic = resp.text
    
    headName = re.findall('<h1>(.*?)</h1>',html_pic)
    print(headName)
    
    if not os.path.exists(str(headName)):
        os.mkdir(str(headName))
        