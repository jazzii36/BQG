import re
import lxml
import time
import csv
from  lxml import etree
import requests
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
}


# 该方法用来获取所有网站所有小说
def GetNovel():
# 获取当前该小说类目下最大分页值
    url = 'https://m.um16.cn/sort-1-1/'
    xhres=requests.get(url=url,headers=headers).content.decode("gbk")
    novelmax=re.findall(".*第1/(.*?)页",xhres)
    maxnovel=int(novelmax[0])
    # print(maxnovel)

# 获取小说列表
    n=1
    xhdatas=[]
    while n<maxnovel:
        url = 'https://m.um16.cn/sort-1-' + str(n) + '/'
        xhres=requests.get(url=url,headers=headers).content.decode("gbk")
        xhtree=etree.HTML(xhres)
        xhdata=xhtree.xpath("/html/body/div[@class='cover']//p/a[2]/@href|/html/body/div[@class='cover']//p/a[2]/text()|/html/body/div[@class='cover']//p/a[3]/text()")
        xhdatas.extend(xhdata)
        n=n+1
        time.sleep(5)

#格式化存储CSV
    header_list = ["Url", "书名", "作者"]
    a=len(xhdatas)
    b=[xhdatas[i:i+3]for i in range(0,a,3)]
    with open("new_data.csv", mode="w", encoding="utf-8-sig", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(header_list)
        writer.writerows(b)
        file.close()


