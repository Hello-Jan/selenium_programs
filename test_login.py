import HTMLTestRunner
import os
import unittest
from time import sleep
from selenium import webdriver

class WyzxwLogin(unittest.TestCase):
    def setUp(self):
        pf=webdriver.FirefoxProfile(r'C:\Users\ckx\AppData\Roaming\Mozilla\Firefox\Profiles\7q1femau.default')
        self.driver=webdriver.Firefox(pf)
        url='https://www.51zxw.net/login'
        self.driver.get(url)
    def test_right_input(self):
        self.driver.find_element_by_css_selector('#loginStr').send_keys('13858477586')
        self.driver.find_element_by_css_selector('#pwd').send_keys('jxm150051')
        self.driver.find_element_by_css_selector('.btn.radius.size-L.btn-danger').click()
        sleep(3)#webdriver.current_url更新的速度比网页更新的速度慢，所以必须延长一定时间，driver对象更新完毕以后 再检测page_source中的内容。
        self.assertIn("jxm372969300",self.driver.page_source)
    def test_just_input_account_number(self):
        self.driver.find_element_by_css_selector('#loginStr').send_keys('13858477586')
        self.driver.find_element_by_css_selector('.btn.radius.size-L.btn-danger').click()
        sleep(3)#webdriver.current_url更新的速度比网页更新的速度慢，所以必须延长一定时间，driver对象更新完毕以后 再检测page_source中的内容。
        self.assertIn("密码不能为空",self.driver.page_source)
    def test_input_wrong_massage(self):
        self.driver.find_element_by_css_selector('#loginStr').send_keys('13858477586')
        self.driver.find_element_by_css_selector('#pwd').send_keys('123')
        self.driver.find_element_by_css_selector('.btn.radius.size-L.btn-danger').click()
        sleep(3)#webdriver.current_url更新的速度比网页更新的速度慢，所以必须延长一定时间，driver对象更新完毕以后 再检测page_source中的内容。
        self.assertIn("登录失败，请检查登录信息是否有误",self.driver.page_source)
    def test_only_input_password(self):
        self.driver.find_element_by_css_selector('#pwd').send_keys('jxm150051')
        self.driver.find_element_by_css_selector('.btn.radius.size-L.btn-danger').click()
        sleep(3)#webdriver.current_url更新的速度比网页更新的速度慢，所以必须延长一定时间，driver对象更新完毕以后 再检测page_source中的内容。
        self.assertIn("请输入账号信息",self.driver.page_source)

    def tearDown(self):
        # self.driver.delete_all_cookies() 浏览器关闭以后，cookies也没有了。
        self.driver.quit()

if __name__=='__main__':
    dir= os.path.dirname(__file__)
    mytests=unittest.defaultTestLoader.discover(dir,pattern='test_login.py')
    f=open(r'F:\pycharmfile\test_web\test_login.html','wb')
    runner= HTMLTestRunner.HTMLTestRunner(stream=f,title='selenuim web自动化测试',description='测试网站登录页面登录表格功能')
    runner.run(mytests)
