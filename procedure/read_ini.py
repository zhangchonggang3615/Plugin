#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 2019/10/8 0008 下午 7:36
# Author : zhangchonggang
# File : read_ini.py
# email: 381057787@qq.com
# software: PyCharm
import configparser

class ReadIni(object):
	def __init__(self,driver,filename=None):
		self.driver=driver
		self.config=configparser.ConfigParser()
		if filename==None:
			self.config.read(r'E:\ztx_test\config\ztx_config.ini')
		else:
			self.config.read(filename)
	def get_url(self,environment=None):
		if environment==None:
			self.driver.get(self.config.get('url','online'))
		else:
			self.driver.get(self.config.get('url',environment))
	def get_element(self,node,element):
		data = self.config.get(node,element)
		by=data.split('>')[0]
		value=data.split('>')[1]
		if by=='id':
			return self.driver.find_element_by_id(value)
		elif by=='name':
			return self.driver.find_element_by_name(value)
		elif by=='class':
			return self.driver.find_element_by_class_name(value)
		elif by=='xpath':
			return self.driver.find_element_by_xpath(value)
		elif by=='partial_link':
			return self.driver.find_element_by_partial_link_text(value)
		elif by=='css':
			return self.driver.find_element_by_css_selector(value)
		elif by=='tag':
			return self.driver.find_element_by_tag_name(value)
		elif by=='link':
			return self.driver.find_element_by_link_text(value)
# if __name__ == '__main__':
#     readini=ReadIni()
#     print(readini.get_element('load_method','zhdl'))
