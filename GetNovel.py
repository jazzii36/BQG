import re
import time
from  lxml import etree
import requests
import csv

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
    n=1
    with open(file="xhtxt.csv", mode="w", encoding="utf-8-sig", newline="") as f:
        header=["urls","bookname","author"]
        writer = csv.writer(f)
        writer.writerow(header)
        while n<maxnovel:
                url = 'https://m.um16.cn/sort-1-' + str(n) + '/'
                xhres=requests.get(url=url,headers=headers).content.decode("gbk")
                xhtree=etree.HTML(xhres)
                xhurl=xhtree.xpath("/html/body/div[@class='cover']//p/a[2]/@href")
                xhbookname=xhtree.xpath("/html/body/div[@class='cover']//p/a[2]/text()")
                xhauthor=xhtree.xpath("/html/body/div[@class='cover']//p/a[3]/text()")
                time.sleep(3)
                # print(xhurl,xhbookname,xhauthor)
                print("第{}页数据获取成功,总计{}页，20条/页".format(n,maxnovel))
                n =n+1
                for urls,bookname,author in zip(xhurl,xhbookname,xhauthor):
                    a=[urls,bookname,author]
                    writer.writerow(a)
                    # print('成功写入一条新数据{}'.format(str(a)))
        f.close()

