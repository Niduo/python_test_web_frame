# -*- coding: utf-8 -*-
"""
by: 老屋
des: 封装页面查找元素基类
"""
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def open_(self, url_):
        self.driver.get(url_)

    def by_id_(self, id_):
        return self.driver.find_element_by_id(id_)

    def by_name_(self, name_):
        return self.driver.find_element_by_name(name_)

    def by_class_(self, class_name_):
        return self.driver.find_element_by_class_name(class_name_)

    def by_xpath_(self, xpath_):
        return self.driver.find_element_by_xpath(xpath_)

    def by_link_text_(self, link_text_):
        return self.driver.find_element_by_link_text(link_text_)

    def page_down_(self):
        k = Keys()
        k.PAGE_DOWN

    def page_up_(self):
        key = Keys.PAGE_UP
        return key

    def get_text(self, by_method, value):
        if by_method == "id":
            self.by_id_(value).text
        elif by_method == "xpath":
            value = self.by_xpath_(value).text
            print(value)
            return value
        elif by_method == "class_name":
            self.by_class_(value).text
        elif by_method == "name":
            self.by_name_(value).text
        else:
            print("输入的查找方式%s不正确：" % by_method)
            return False



