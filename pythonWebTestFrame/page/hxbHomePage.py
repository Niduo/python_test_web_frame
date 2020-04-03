# -*- coding: utf-8 -*-
"""
by: 老屋
des: 定位及操作hxb首页元素
"""
from page.basePage import BasePage
from selenium.webdriver.common.keys import Keys
import time


class HxbHomePage(BasePage):
    def plan_link(self):
        # 首页定位红利智投
        self.by_xpath_("/html/body/div[2]/div/div[2]/ul/li[2]/a").click()
        time.sleep(2)
        # 用js命令实现滚动页面
        js = "return arguments[0].scrollIntoView();"
        element_ = self.by_xpath_('/html/body/div[3]/div[2]/div[1]/div[3]/div/dl[4]/a')
        self.driver.execute_script(js, element_)

    def plan_link_res(self):
        result = []
        # 获取'本息复投 按月提取收益' 字符
        text1 = self.get_text("xpath", "/html/body/div[3]/div[2]/div[1]/div[2]/h4")
        text2 = self.get_text("xpath", "/html/body/div[3]/div[2]/div[1]/div[3]/h4")
        result.append(text1)
        result.append(text2)
        # print(text1, text2, result, type(result))
        return result

    def loan_link(self):
        self.by_xpath_("/html/body/div[2]/div/div[2]/ul/li[3]/a").click()
        time.sleep(2)
        self.by_xpath_('//*[@id="loan-list"]/div[2]/ul/li[1]/a').send_keys(Keys.PAGE_DOWN)

    def loan_link_res(self):
        result = []
        # 获取'散标出借， 债权转让'字符
        text1 = self.get_text("xpath", '//*[@id="loan-list"]/div[2]/ul/li[1]/a')
        text2 = self.get_text("xpath", '/html/body/div[3]/div[2]/ul/li[2]/a')
        result.append(text1)
        result.append(text2)
        # print(text1, text2, result, type(result))
        return result