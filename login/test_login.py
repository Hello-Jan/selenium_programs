#-*- coding:utf-8 -*-
'''
本项目使用unittest模块测试我要自学网的登录页面的功能
'''

import HTMLTestRunner
import os
import unittest
from time import sleep
from selenium import webdriver

class MyzxwLogin(unittest.TestCase):
    #在每个测试用例前执行：打开浏览器、打开自学网登录页面。
    def setUp(self):
        pf=webdriver.FirefoxProfile(r'C:\Users\ckx\AppData\Roaming\Mozilla\Firefox\Profiles\7q1femau.default')
        self.driver=webdriver.Firefox(pf)
        url='https://www.51zxw.net/login'
        self.driver.get(url)
    #测试用例1：测试当账号密码都输入正确时是否能成功登录。
    def test_right_input(self):
        self.driver.find_element_by_css_selector('#loginStr').send_keys('13858477586')
        self.driver.find_element_by_css_selector('#pwd').send_keys('jxm150051')
        self.driver.find_element_by_css_selector('.btn.radius.size-L.btn-danger').click()
        sleep(3)#webdriver.current_url更新的速度比网页更新的速度慢，所以必须延长一定时间，driver对象更新完毕以后 再检测page_source中的内容。
        self.assertIn("jxm372969300",self.driver.page_source)
    #测试用例2：测试当只输入账号不输入密码时，网页是否会提示“密码不能为空”。
    def test_just_input_account_number(self):
        self.driver.find_element_by_css_selector('#loginStr').send_keys('13858477586')
        self.driver.find_element_by_css_selector('.btn.radius.size-L.btn-danger').click()
        sleep(3)
        self.assertIn("密码不能为空",self.driver.page_source)
    #测试用例3：测试当输入账号和错误密码时，网页是否会有预期提示。
    def test_input_wrong_massage(self):
        self.driver.find_element_by_css_selector('#loginStr').send_keys('13858477586')
        self.driver.find_element_by_css_selector('#pwd').send_keys('123')
        self.driver.find_element_by_css_selector('.btn.radius.size-L.btn-danger').click()
        sleep(3)
        self.assertIn("登录失败，请检查登录信息是否有误",self.driver.page_source)
    #测试用例4：测试当只输入密码时，网页是否会有预期提示。
    def test_only_input_password(self):
        self.driver.find_element_by_css_selector('#pwd').send_keys('jxm150051')
        self.driver.find_element_by_css_selector('.btn.radius.size-L.btn-danger').click()
        sleep(3)
        self.assertIn("请输入账号信息",self.driver.page_source)
    #在每个测试用例结束后执行：关闭浏览器
    def tearDown(self):
        # self.driver.delete_all_cookies() 浏览器关闭以后，cookies也没有了。
        self.driver.quit()

if __name__=='__main__':
    dir= os.path.dirname(__file__)
    #此方法自动找出所有测试用例
    # mytests=unittest.defaultTestLoader.discover(dir,pattern='test_login.py')
    #通过TestSuite方法可以自定义添加测试用例
    mytests=unittest.TestSuite()
    suite=[MyzxwLogin('test_right_input'),MyzxwLogin('test_just_input_account_number'),MyzxwLogin('test_input_wrong_massage')]
    mytests.addTests(suite)
    f=open(r'F:\pycharmfile\test_web\test_login.html','wb')
    runner= HTMLTestRunner.HTMLTestRunner(stream=f,title='selenuim web自动化测试',description='测试网站登录页面登录表格功能')
    runner.run(mytests)
