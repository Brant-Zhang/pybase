#!/usr/bin/env python
import struct
import binascii
'''
import MYSQLdb

def modirfy(cur):
	cur.execute("select pid,reserved from dnakit_pid")
	stas:=cur.fetchall()

	for st in stas:
		

if __name__ == 'main':
	try :
		conn = MYSQLdb.connect(host="localhost",user="root",passwd="123456",db="mysql",charset="utf-8")
		cur = conn.cursor()
		cur.execute("create database if not exists dnakit default character set utf8")
        cur.execute("use dnakit")
        cur.execute("set names utf8")

        modirfy(cur)
        conn.commit()
        cur.close()
        conn.close()

    except MYSQLdb.Error,e:
    	print e
'''
data="1122334455"

platform=0x8776
startbit=0xaa
length=992
tp=0x08
magic=0x5a5aa5a5

ss=struct.pack('<HBI',platform,tp,length)
print 'packed value:', binascii.hexlify(ss),len(ss)
print ('hello world')

def getsum(data):
	a = 0x0
	for i:=0;i<len(data)/4;i++{
		a = a+ 
	}
