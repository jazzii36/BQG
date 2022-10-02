import re
import time
from  lxml import etree
import requests
import pandas as pd

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
}


# 该方法用来获取所有网站所有小说列表
def GetNovel():
# 获取当前该小说类目下最大分页值
    url = 'https://m.um16.cn/sort-1-1/'
    xhres=requests.get(url=url,headers=headers).content.decode("gbk")
    novelmax=re.findall(".*第1/(.*?)页",xhres)
    maxnovel=int(novelmax[0])
    # print(maxnovel)
    n=1
    while n<maxnovel:
        url = 'https://m.um16.cn/sort-1-' + str(n) + '/'
        xhres=requests.get(url=url,headers=headers).content.decode("gbk")
        xhtree=etree.HTML(xhres)
        xhurl=xhtree.xpath("/html/body/div[@class='cover']//p/a[2]/@href")
        xhbookname=xhtree.xpath("/html/body/div[@class='cover']//p/a[2]/text()")
        xhauthor=xhtree.xpath("/html/body/div[@class='cover']//p/a[3]/text()")
        n=n+1
        time.sleep(5)
        dataframe=pd.DataFrame({"地址":xhurl,"书名":xhbookname,"作者":xhauthor})
        dataframe.to_csv('novellist.csv', index=False, sep=',')
    # else:爬取其他类目

GetNovel()