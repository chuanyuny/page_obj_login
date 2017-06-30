# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class LoginPage(Page):
	'''发布会登录页面模型'''
	url='/'
	#定位器
	username_loc=(By.NAME,"username")
	password_loc=(By.NAME,"password")
	submit_loc=(By.ID,"btn")

	#Action
	def type_username(self,username):
		self.find_element(*self.username_loc).send_keys(username)

	def type_password(self,password):
		self.find_element(*self.password_loc).send_keys(password)

	def submit(self):
		self.find_element(*self.submit_loc).click()

	#定义用户统一登录入口
	def user_login(self,username='admin',password='123456'):
		self.open()
		self.type_username(username)
		self.type_password(password)
		self.submit()

	def user_txt(self):
		return self.find_element(*self.username_loc).text

	def pas_txt(self):
		return self.find_element(*self.password_loc).text




