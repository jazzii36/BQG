import encodings

import lxml
import time
import csv
from  lxml import etree
import requests
import re

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
}

# 该方法用来爬取某章节下所有页面的数据
def getchapterdata(url,novelname):
    chapterdate = requests.get(url=url, headers=headers).content.decode("gbk")
    chapterdatetree=etree.HTML(chapterdate)
    # 取文章分页最大值maxnum
    max=chapterdatetree.xpath('/html/body/div[2]/div[2]/text()')
    maxnum=max[0].strip()
    print(maxnum[-2])
    folmatdata = ""

    for i in range (1,int(maxnum[-2])+1):
        url2="https://m.um16.cn/book/86220/44018708"+"_"+str(i)+".html"
        print(url2)
        chapterdate2 = requests.get(url=url2, headers=headers).content.decode("gbk")
        chapterdatetree2 = etree.HTML(chapterdate2)
        data=chapterdatetree2.xpath('//*[@id="nr1"]/text()')
        for string in data :
                string2=str(string).strip()
                string2=string2.replace("【笔趣阁　】为您提供最快更新！","")
                string2 = string2.replace("，为您。", "")
                string2=string2.replace("手机用户请浏览m.1biquge.　阅读，更优质的阅读体验。","")
                if string2 !="":
                    folmatdata =folmatdata+string2
    print(folmatdata)
    with open(file="{}".format(novelname), mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(folmatdata)
        f.close()


