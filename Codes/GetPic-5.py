import requests as req, re, os


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


def get_picture(picUrl):
    html = req.get(url= picUrl, headers= headers).text
    urls = re.findall('<div class="il_img"><a href=".*?"'
            'target="_blank"><img src="(.*?)" alt= ".*?">', html)
    
    for url in urls:
        picUrl   = 'https://www.ivsky.com' + url
        htmlPic  = req.get(url= picUrl, headers= headers).text
        headName = re.findall('<h1(.*?)></h1>', htmlPic)
        
        if not os.path.exists(str(headName)):
             os.mkdir(str(headName))
             
        downloadPics(htmlPic, headName)
        

def downloadPics(htmlPic, headName):
    pics = re.findall('<div class="il_img"><a href=".*?"'
            'target="_blank"><img src="(.*?)" alt= ".*?">', htmlPic)
    
    for pic in pics:
        fileName = pic.split('/')[-1]
        pic = 'https:' + pic
        picContent = req.get(pic, headers= headers).content
        
        with open (str(headName) + '/' + fileName, 'wb') as f:
            f.write(picContent)
            
    nextPage = re.findall("a class= 'page-next' href= '(.*?)'> 下一页</a>", htmlPic)
    
    if nextPage:
        for url in nextPage:
            url = "https://www.ivsky.com/" + url
            content = req.get(url= url, headers= headers).text
            downloadPics(content, headName)
    
    
if __name__ == '__main__':
    urlPic = 'https://www.ivsky.com/tupian/haiyangshijie'
    
    for i in range(1):
        if i == 1:
            pass

        else:
            url = urlPic + "index_" + str(i) + "html"
            get_picture(url)

# ██████╗  ███████╗██╗     ██╗   ██╗ ██████╗  █████╗ ███╗   ███╗ █████╗ ███╗   ██╗
# ██╔══██╗ ██╔════╝██║     ██║   ██║██╔════╝ ██╔══██╗████╗ ████║██╔══██╗████╗  ██║
# ██████╔╝ █████╗  ██║     ██║   ██║██║  ██╗ ███████║██╔████╔██║███████║██╔██╗ ██║
# ██╔══██╗ ██╔══╝  ██║     ██║   ██║██║  ╚██╗██╔══██║██║╚██╔╝██║██╔══██║██║╚██╗██║
# ██████╔╝ ███████╗███████╗╚██████╔╝╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║
# ╚═════╝  ╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝