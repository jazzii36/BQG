import csv

import GetNovel,GetChapter,GetchapterDate



# if __name__=='main':
    # GetNovel.GetNovel()
with open("new_data.csv",'r',encoding='utf-8') as fia:
    rea=csv.DictReader(fia)
    for x in rea:
        print(x["作者"])

