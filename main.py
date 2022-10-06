import csv
import GetNovel,GetChapter,GetchapterDate
import mysql.connector



bqg = mysql.connector.connect(
  database="bqg",
  host="localhost",
  user="bqg",
  passwd="88840288",
auth_plugin='mysql_native_password'
)
mycursor = bqg.cursor()
sql="SELECT bookname,urls FROM xhnovel "
mycursor.execute(sql)
results=mycursor.fetchall()
for re in results:
  GetChapter.Getchapter(url=re[1],novelname=re[0])