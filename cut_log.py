#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Copyright (C) 2013 Edgewall Software
#
#  Authors:   
#    guo.lei@autonavi.com  < http://www.weibo.com/u/2001677023 > <qq:674653>
from xml.dom import minidom
import sys
import os
import subprocess
import zipfile

def getLogList():
        try:
    dom = minidom.parse('log_path.xml')
        except BaseException, e:
                print e
                sys.exit()
	node_root = dom.documentElement
        node_list = node_root.getElementsByTagName("log")
	for node in node_list:
                path_node = node.getElementsByTagName("path")[0]
                path_value = path_node.childNodes[0].data
                save_path_node = node.getElementsByTagName("save")[0]
                save_path_value = save_path_node.childNodes[0].data
		days_node = node.getElementsByTagName("days")[0]
                days_value = days_node.childNodes[0].data
		name_node = node.getElementsByTagName("name")[0]
                name_value = name_node.childNodes[0].data
		import_log(path_value,save_path_value,name_value)
		del_exceed_log (save_path_value,days_value)

def import_log(path,save,name): 
	time = subprocess.Popen("date +'%Y-%m-%d'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	date = time.stdout.read().rstrip()
	rp = open(path,'r')
	rf = rp.read().strip()
	wp = open('%s/%s-%s' %(save,name,date),'w')
	wf = wp.write(rf)
	rp.close()
	wp.close()
	qp = open(path,'w')
	qp.truncate()
	qp.close()
	f = zipfile.ZipFile('%s/%s-%s.zip' %(save,name,date),'w',zipfile.ZIP_DEFLATED,allowZip64=True)
	f.write('%s/%s-%s' %(save,name,date))
	f.close
	os.remove('%s/%s-%s' %(save,name,date))
	
def del_exceed_log(save,days):
	os.system('find %s -type f -mtime +%s -exec rm -fr {} \;' %(save,days))
	
#------------------------- start---------------------------
if __name__ == '__main__':
    getLogList()
	#pass
