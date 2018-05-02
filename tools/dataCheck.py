#!/usr/bin/python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import pprint
import smtplib
from email.mime.text import MIMEText

conn = MongoClient('127.0.0.1', 27017)
db = conn.steplog  #连接mydb数据库，没有则自动创建
se=db.session
tn=db.tunnel_info
def query():
    notice = []
    result = ''
    i=tn.find_one({"last_send_bytes":{"$lt":0}})
    notice.append(i)
    result=str(i)
    i=se.find_one({"tx_bytes":{"$lt":0}})
    notice.append(i)
    result=str(i)
    pprint.pprint(result)
    email_send(result)
    return


def email_send(val):
    msg=MIMEText(val)
    me='15158134537@139.com'
    targets=['zhanglei@supercxp.com','brantzha@gmail.com']
    msg['Subject'] = 'logbase alert'
    msg['From'] = me
    #msg['To'] = you
    server = smtplib.SMTP('smtp.139.com', 25)
    #server.starttls()
    server.login(me, 'xxxx')
    server.sendmail(me, targets, msg.as_string())
    server.quit()

if __name__ == "__main__":
    query()
    #email_send('hello world4')
