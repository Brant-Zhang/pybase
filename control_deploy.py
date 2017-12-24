#!/usr/bin/python
#coding=utf-8
__version__ = "0.1"
__all__ = ["SimpleHTTPRequestHandler"]
__author__ = "zhangl"
__home_page__ = ""

import os, sys
import posixpath
import BaseHTTPServer
from SocketServer import ThreadingMixIn
import threading
import urllib
import cgi
import shutil
import mimetypes
import re
import time
#from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
import time
import ConfigParser
import json
import hashlib

from fabric.context_managers import *

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

result={}
defaultval="{\"code\":1,\"msg\":\"no record right now!\"}"
blpath="/home/brant/temp"
#blname="blcloudstack.deb"
confname="/etc/autodeploy.ini"

try:
   port = int(sys.argv[1])
except Exception, e:
   port = 9000

serveraddr = ('', port)

def depackage():
    os.chdir(blpath)
    try:
    	local("rm -rf ./debian/;mkdir ./debian")
   	local("dpkg -x ./blcloudstack.deb ./debian")
    	local("mkdir ./debian/DEBIAN; dpkg -e ./blcloudstack.deb ./debian/DEBIAN")
    	local('cp ./debian/etc/blcloudstack.conf ./debian/etc/blcloudstack.conf_main;cp ./debian/etc/blcloudstack.conf ./debian/etc/blcloudstack.conf_backup')
    except:
	return -1
    return 0

def modifyconf(mo,mi,bo,bi):
    node ="ufastrelay"
    conf = ConfigParser.ConfigParser()
    conf.optionxform = str
    os.chdir(blpath)
    try:
    	conf.read("./debian/etc/blcloudstack.conf_main")
    	conf.set(node,'outAddr',mo+':16384')
    	conf.set(node,'innerAddr',mi+':7779')
    	conf.write(open("./debian/etc/blcloudstack.conf_main" , "w"))

    	conf.read("./debian/etc/blcloudstack.conf_backup")
    	conf.set(node,'outAddr',bo+':1812')
    	conf.set(node,'innerAddr',bi+':7779')
    	conf.write(open("./debian/etc/blcloudstack.conf_backup","w"))
    except :
	print "modify configure file failed"
	return -1
    return 0

def package():
    os.chdir(blpath)
    local('dpkg-deb --build ./debian')
    local('mv ./debian.deb ./blcloudstack.deb')

def set_hosts(user,name,ps):
    env.hosts=[user+'@'+name+':22']
    env.password=ps

def pdeploy(flag):
    ret="{\"code\":0,\"msg\":\"success!\"}"
    reterr="{\"code\":-2,\"msg\":\"please check the servers you provided\"}"
    try:
    	lcd(blpath)
    	put("blcloudstack.deb","/root/blcloudstack.deb")
    except:
	return reterr

    run('stop supercache;stop ufastrelay',warn_only=True)

    try:
    	run('dpkg -i blcloudstack.deb')
    	run('mv /etc/blcloudstack.conf_%s /etc/blcloudstack.conf' %flag)
    	if flag=='main':
        	run('cp /usr/local/etc/supercache.conf /etc/init/supercache.conf ;start supercache')
		output=run("ps -ef |grep 'supercache' |grep -v 'grep'",warn_only=True)
		if output.return_code !=0 :
		    return reterr
        	time.sleep(1)
    	run('cp /usr/local/etc/ufastrelay.conf /etc/init/ufastrelay.conf;start ufastrelay')
	output=run("ps -ef |grep 'ufastrelay' |grep -v 'grep'",warn_only=True)
	if output.return_code !=0 :
            return reterr
    except:
	ret=reterr

    return ret

def deploy(djson):
    ret="{\"code\":0,\"msg\":\"success!\"}"
    #djson=json.loads(serverinfo)
    try:
    	moip=djson["main"]["oip"]
    	miip=djson["main"]["iip"]
    	boip=djson["backup"]["oip"]
    	biip=djson["backup"]["iip"]
    	muser=djson["main"]["user"]
    	mpasswd=djson["main"]["password"]
    	buser=djson["backup"]["user"]
    	bpasswd=djson["backup"]["password"]

    except KeyError:
	ret="{\"code\":-1,\"msg\":\"parameters not complete\"}"
    	return ret
    if depackage()!=0 or modifyconf(moip,miip,boip,biip)!=0 :
	ret="{\"code\":-3,\"msg\":\"server busy\"}"
	return ret

    package()
    with settings(parallel=True,host_string=muser+'@'+moip+':22'):
	env.password=mpasswd
	env.user=muser
	#upload()
    	ret=pdeploy("main")
	#env.host_string = 'otherhost'

    jdata=json.loads(ret)
    if jdata["code"] == 0 :
    	with settings(parallel=True,host_string=buser+'@'+boip+':22'):
	    env.password=bpasswd
	    env.user=buser
    	    #upload()
    	    ret=pdeploy("backup")

    return ret

#env.key_filename = "/home/ubuntu/omg.pem"
class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    server_version = "SimpleHTTPWithUpload/" + __version__

    def do_GET(self):
	#print "recv get----------------",self.path
	mpath,margs=urllib.splitquery(self.path)
	if mpath == "/dnakit/server/query" :
	    if self.checkHead(mpath):
	    	self.query_deploy(margs)
	else:
	    print "get request path not valid:",self.path

    def do_POST(self):
	pa = self.path
	if not self.checkHead(self.path):
	    print "not authed"
	    return
	if pa == "/dnakit/server/deploy":
	    self.deploy_server()
	else:
	    print "post request path not valid:",pa

    def checkHead(self,route):
        t=self.headers.get("timestamp","")
        s=self.headers.get("sign","")

        shastr = route+str(t)+"broadlinkDNA@"
        hash_new = hashlib.sha1()
        hash_new.update(shastr)
        token = hash_new.hexdigest()

        #print "+++++++++++++++",t,s,shastr,token
        return s==token

    def deploy_server(self):
	buf='{\"code\":0,\"msg\":\"ok\"}'
	astatus=True
	datas = self.rfile.read(int(self.headers['content-length']))
	djson=json.loads(datas)
	try:
	    vid=djson["vendor_id"]
	except KeyError:
	    buf="{\"code\":-1,\"msg\":\"no vendor id\"}"
	    astatus=False

        buf=buf.encode()
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=UTF-8')
        self.send_header("Content-Length",str(len(buf)))
        self.end_headers()
        #self.request.send(buf)
        self.wfile.write(buf)
	if astatus :
            ret=deploy(djson)
            result[vid]=ret

    def query_deploy(self,margs):
	vid=margs.split('=',1)[1]
	#print vid
	if result.has_key(vid):
	    buf=result.get(vid)
	else:
	    buf=defaultval
        buf=buf.encode()
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=UTF-8')
        self.send_header("Content-Length",str(len(buf)))
        self.end_headers()
        #self.request.send(buf)
        #print "query response"
        self.wfile.write(buf)

class ThreadingServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass

def test(HandlerClass = SimpleHTTPRequestHandler,
       ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)

def read_conf():
    if len(sys.argv)==2:
        confname = str(sys.argv[1])
    else:
        confname = "/etc/autodeploy.ini"

    node ="deploy"

    conf = ConfigParser.ConfigParser()
    conf.optionxform = str
    conf.read(confname)
    port = conf.get(node,"listen_port")
    blpath = conf.get(node,"bl_filepath")
    #blname = conf.get(node,"bl_filename")
    print port ,blpath


if __name__ == '__main__':
    # test()
    read_conf()
    #单线程
    srvr = BaseHTTPServer.HTTPServer(serveraddr, SimpleHTTPRequestHandler)

    #srvr = ThreadingServer(serveraddr, SimpleHTTPRequestHandler)
    srvr.serve_forever()
