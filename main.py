import lxml
from  lxml import etree
import requests
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
}

# 获取小说列表
n=1
xhdatas=[]
while n<18:
    url = 'https://m.um16.cn/sort-1-' + str(n) + '/'
    xhres=requests.get(url=url,headers=headers).content.decode("gbk")
    xhtree=etree.HTML(xhres)
    xhdata=xhtree.xpath("/html/body/div[@class='cover']//p/a[2]/@href|/html/body/div[@class='cover']//p/a[2]/text()|/html/body/div[@class='cover']//p/a[3]/text()")
    xhdatas.extend(xhdata)
    n=n+1
print(xhdatas)

# 获取小说章节
urlclumb="https://m.um16.cn“+/book/51385_1.html"

