# -*- coding:utf-8 -*-

'''
本函数用于测试智联招聘网站切换城市功能、查找工作信息功能,并可将结果打印出来或者输入到excel表格。
'''

import selenium
from selenium import webdriver
import xlwt
from time import sleep

#自定义一个函数，使目标文档在原窗口中打开。
def set_self_for_target_and_click(driver,element):
        driver.execute_script("arguments[0].target='_self'",element)
        element.click()

class Job(object):
    def __init__(self,profile=None):
        self.pf=None
        if profile is not None:
            self.pf=webdriver.FirefoxProfile(profile)
        #打开浏览器
        self.driver=webdriver.Firefox(self.pf)
        self.driver.implicitly_wait(3)
    '''
    just_test参数：默认调用此方法时该参数为空，则浏览器不会关闭。
    如果只是单纯测试一下，不是给其他项目调用，则将该参数设置为非空,测试结束时，浏览器自动关闭。
    '''
    def test(self,job='测试工程师',city=None,just_test=None):
        #打开智联招聘首页
        url='https://www.zhaopin.com/'
        self.driver.get(url)
        #消除警告窗口
        self.driver.find_element_by_css_selector('.risk-warning__content>button').click()
        #如果有指定city参数则进行设定城市的操作
        if city is not None:
            element=self.driver.find_element_by_css_selector('.zp-city__change')
            set_self_for_target_and_click(self.driver,element)
            #如果输入的城市无法识别，则捕获错误，抛出提示：“城市名输入有误！请重新输入。”
            try:
                element1=self.driver.find_element_by_partial_link_text(city)
            except selenium.common.exceptions.NoSuchElementException:
                print('亲爱的测试小伙伴：您的城市名输入有误！请重新输入。')
            set_self_for_target_and_click(self.driver,element1)
        #输入工作名称
        self.driver.find_element_by_css_selector('.zp-search__input').send_keys(job)
        self.driver.find_element_by_css_selector('.zp-search__btn.zp-search__btn--blue').click()
        #将获取新的窗口
        self.driver.switch_to.window(self.driver.window_handles[1])
        if just_test is not None:
            self.driver.quit()

    #将结果以一定的格式打印出来。separator参数设定分隔符，rows参数设定打印多少行
    def print(self,job='测试工程师',city=None,separator='|',rows=10):
        self.test(job,city) #获取test方法返回的结果
        eles = self.driver.find_elements_by_css_selector('#listContent .contentpile__content__wrapper.clearfix')
        if isinstance(rows,int):
            eles_p=eles[:rows]
        #当输入的rows参数非整数时，默认打印全部结果
        else:
            eles_p=eles
        for ele in eles_p:
            L=list()
            for x in ['.jobName','.commpanyName','.contentpile__content__wrapper__item__info__box__job__saray']:
                s=ele.find_element_by_css_selector(x).text
                L.append(s)
            res=separator.join(L)
            print(res)
        self.driver.quit()

    #将结果导出到excel，调用本方法需要先传入locaton参数，以确定文件存放位置。
    def export_excel(self,location,job='测试工程师',city=None):
        #初始化表格
        book=xlwt.Workbook()
        sh=book.add_sheet('统计')
        row=0
        self.test(job,city)
        eles=self.driver.find_elements_by_css_selector('#listContent .contentpile__content__wrapper.clearfix')
        for ele in eles:
            col=0
            for x in ['.jobName','.commpanyName','.contentpile__content__wrapper__item__info__box__job__saray']:
                s=ele.find_element_by_css_selector(x).text
                sh.write(row,col,s)
                col+=1
            row+=1
        book.save(location)
        self.driver.quit()


if __name__ == '__main__':
    '''
    您的配置文件位置可按此方法找到：火狐浏览器--打开帮助菜单--排除故障信息--配置文件--显示文件夹。
    此处需注意反斜杠'\'（转义字符）在字符串中的表示方法。
    '''
    # pf=r'C:\Users\ckx\AppData\Roaming\Mozilla\Firefox\Profiles\7q1femau.default'
    # job=Job(pf)
    job=Job()
    # job.test('测试工程师','深圳',just_test=1)
    # sleep(5)
    job.print('测试工程师','北京')
    # sleep(5)
    # location=r'f:\pycharmfile\test_web\jobs.xls'
    # job.export_excel(location,'测试工程师','北京')



