import lxml
import time
import csv
from  lxml import etree
import requests
import re
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
}


# 该方法用来爬取某文章所有章节
chapterdatas=[]
def Getchapter(url,novelname):
    url1 = "https://m.um16.cn"+url[0:-5]+"_1.html"
    print(url1)
    chapterres = requests.get(url=url1, headers=headers).content.decode("gbk")
    print(url1,chapterres)
    # 获取所有章节最大分页值
    pattern = "第1/(.*?)页"
    chaptermax=re.findall(pattern, chapterres)
    print(novelname,chaptermax)
    # 爬取所有章节目录数据
    for n in range(1,int(chaptermax[0])+1):
        url2 = "https://m.um16.cn"+url[0:-5]+"_"+str(n)+".html"
        chapterres = requests.get(url=url2, headers=headers).content.decode("gbk")
        # print(chapterres)
        # 获取每一个章节目录数据
        chaptertree = etree.HTML(chapterres)
        chapterdata = chaptertree.xpath("/html/body/div[@class='cover']/ul//li/a/text()|/html/body/div[@class='cover']/ul[@class='chapter']//li/a/@href")
        # print(chapterdata)
        chapterdatas.extend(chapterdata)
    print(chapterdatas)
    # 章节数据格式化存储csv
    with open(file="{}Chapter.csv".format(novelname), mode="w", encoding="utf-8-sig", newline="") as f:
        headerstable=["Url","chaptername"]
        a = len(chapterdatas)
        b = [chapterdatas[i:i + 2] for i in range(0, a, 2)]
        writer = csv.writer(f)
        writer.writerow(headerstable)
        writer.writerows(b)
        f.close()

