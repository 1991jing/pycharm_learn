#coding=utf-8
from selenium import webdriver
import pymysql



class mysql():
    def __init__(self):
        self.conn=pymysql.connect(host="192.168.9.111",port=3306,user="root",passwd="123456",
                                  use_unicode=True,charset="utf8")
        self.cur=self.conn.cursor()


    def select_step(self,sql):
        self.cur.execute(sql)
        resultdata=self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return resultdata

    def dml_step(self,sql):
        self.cur.execute(sql)
        self.cur.close()
        self.conn.close()


if __name__=="__main__":
    sql ="SELECT a.`username`,a.`password` FROM admin.`t_admin` a WHERE realname='jing';"
    sql2="SELECT SUBSTRING((SELECT content FROM jld_message.t_sms_record WHERE content_type = 'REGISTER' ORDER BY create_time DESC LIMIT 1,1),8,4);"
    SQL=mysql()
    #a=SQL.select_step(sql)
    b=SQL.select_step(sql2)
   # print(a)
    print(b)
    #print(a[0][0])
    #print(a[0][1])