import urllib.request, re
from urllib import request


def getPicHtml(url):
    with request.urlopen(url) as f:
        content = f.read()
        return content;
        
    
def createImg(content):
    reg = r'src="(.+?\.jpg)" pic_ext'
    content = content.decode('utf-8')
    imgList = re.findall(reg, content)
    i = 0

    for imgurl in imgList:
        urllib.request.urlretrieve(imgurl, '../%s.jpg' %i)
        i += 1


if __name__ == '__main__':
    url = "https://tieba.baidu.com/p/2555125530?pn=1"
    content = getPicHtml(url)
    createImg(content)
    
    