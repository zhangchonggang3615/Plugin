#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 2019/10/8 0008 下午 8:02
# Author : zhangchonggang
# File : ztx_main.py
# email: 381057787@qq.com
# software: PyCharm
import os,time
from selenium import webdriver
from procedure.read_ini import ReadIni
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class ztx_zbr(object):
	'''招标人角色系统流程'''
	def __init__(self,driver=None):
		if driver==None or driver=='firefox':
			self.driver=webdriver.Firefox()
		elif driver=='chrome':
			self.driver=webdriver.Chrome()
		else:
			self.driver=webdriver.Ie()
		self.driver.maximize_window()
	def Instaniation(self,driver=None,filename=None):
		cf = ReadIni(filename,driver=self.driver)
		return cf
	def login_page(self,enviroment=None,node='loginpage'):
		self.Instaniation().get_url(enviroment)#打开登录页面
		self.Instaniation().get_element(node,'zhdl').click()#选择登录方式
		self.Instaniation().get_element(node,'username').send_keys('cstbr8')
		self.Instaniation().get_element(node,'password').send_keys('user1234')
		self.Instaniation().get_element(node,'login').send_keys(Keys.ENTER)
		self.driver.implicitly_wait(5)
	def NewProject(self,node='xmgl'):
		ActionChains(self.driver).click(self.Instaniation().get_element(node,'xmgl')).perform()
		ActionChains(self.driver).click(self.Instaniation())
	def run(self):
		try:
			self.login_page()
			self.NewProject()
		except BaseException as BE:
			print(BE.args)
		finally:
			time.sleep(5)
			# self.driver.quit()
if __name__ == '__main__':
    zbr = ztx_zbr('chrome')
    zbr.run()

