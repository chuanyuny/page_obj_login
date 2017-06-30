# -*- coding: utf-8 -*-
from time import sleep,strftime
import unittest,random,sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit,function
from page_obj.loginPage import LoginPage
from selenium.webdriver.common.by import By
from HTMLTestRunner import HTMLTestRunner
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class loginTest(myunit.MyTest):
	'''社区登录测试'''

	#测试用户登录
	def user_login_verify(self,username="",password=""):
		LoginPage(self.driver).user_login(username,password)

	def now_time(self):
		now=strftime("%Y-%m-%d %H_%M_%S")
		return now

	def test_login1(self):
		'''用户名，密码为空登录'''
		self.user_login_verify()
		po=LoginPage(self.driver)
		self.assertEqual(po.user_txt(),'')
		self.assertEqual(po.pas_txt(),'')
		function.insert_img(self.driver,'user_pwd_empty'+self.now_time()+'.jpg')

	def test_login2(self):
		'''用户名正确,密码为空登录'''
		self.user_login_verify(username='admin')
		po=LoginPage(self.driver)
		self.assertEqual(po.pas_txt(),'')
		function.insert_img(self.driver,'pwd_empty'+self.now_time()+'.jpg')

	def test_login3(self):
		'''用户名为空,密码正确'''
		self.user_login_verify(password='123456')
		po=LoginPage(self.driver)
		self.assertEqual(po.user_txt(),'')
		function.insert_img(self.driver,'user_empty'+self.now_time()+'.jpg')

	def test_login4(self):
		'''用户名,密码正确'''
		self.user_login_verify(username='admin',password='123456')
		sleep(3)
		po=LoginPage(self.driver)
		txt=(By.XPATH,"/html/body/nav/div/div[1]/a")
		text=po.find_element(*txt).text
		self.assertEqual(text,'Guest Manage System')
		function.insert_img(self.driver,'user_pas_correct'+self.now_time()+'.jpg')

if __name__=='__main__':
	# unittest.main()
	testunit=unittest.TestSuite()
	testunit.addTest(loginTest('test_login1'))
	testunit.addTest(loginTest('test_login2'))
	testunit.addTest(loginTest('test_login3'))
	testunit.addTest(loginTest('test_login4'))
	now=strftime("%Y-%m-%d %H_%M_%S")
	#以下这4行用于设置相对目录的时候要用的。
	base_dir=os.path.dirname(os.path.dirname(__file__))
	base_dir=str(base_dir)
	base_dir=base_dir.replace('\\',"/")
	base=base_dir.split('test_case')[0]
	filename=base+'/report/'+now+'result.html'
	fp=open(filename,'wb')
	runner=HTMLTestRunner(stream=fp,title="",description="")
	runner.run(testunit)
	fp.close()









































