#!/usr/bin/env python
import MYSQLdb

def addTable(cur):


def modirfy(cur):
    cur.execute("select * from clientset")
    stas:=cur.fetchall()
    for st in stas:
        print st


if __name__ == '__main__':
    try :
	conn = MYSQLdb.connect(host="localhost",user="root",passwd="root",db="mysql",charset="utf-8")
		cur = conn.cursor()
		cur.execute("create database if not exists front default character set utf8")
        cur.execute("use front")
        cur.execute("set names utf8")

        modirfy(cur)
        conn.commit()
        cur.close()
        conn.close()

    except MYSQLdb.Error,e:
    	print e
