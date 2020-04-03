# -*- coding: utf-8 -*-
"""
by: 老屋
des: hxb首页测试用例demo
"""
from common import browserType
from readConfig import ReadConfig
from page.hxbHomePage import HxbHomePage
from common.readxml import Readxml
import pytest
import time


class TestHxbHome:
    @classmethod
    def setup_class(cls):
        cls.hxb_url = ReadConfig().url_hxb()
        cls.wd = browserType.browser("Chrome")
        cls.xml_read = Readxml()
        cls.page = HxbHomePage(cls.wd)

    @classmethod
    def teardown_class(cls):
        browserType.browser_close()

    def setup(self):
        self.page.open_(self.hxb_url)
        time.sleep(2)
        print("launch homepage , start test!")

    def teardown(self):
        time.sleep(2)
        print("test end!")

    def test_plan_link_001(self):
        """
        描述: 确认计划链接有效
        步骤：
        1、首页点击红利智投
        2、搜索本息复投和按月提取收益
        结果：期望的结果和页面字符串可匹配
        :return:
        """
        exp1 = self.xml_read.r_data_hxb("test_plan_link_001", "expect_result1")
        exp2 = self.xml_read.r_data_hxb("test_plan_link_001", "expect_result2")
        self.page.plan_link()
        time.sleep(2)
        actual = self.page.plan_link_res()

        assert actual[0] == exp1, "实际值:%s, 不等于期望值%s" % (actual[0], exp1)
        assert actual[1] == exp2, "实际值:%s, 不等于期望值%s" % (actual[1], exp2)

    def test_loan_link_002(self):
        """
        描述: 确认散标债权链接有效
        步骤：
        1、首页点击红利智投
        2、搜索散标出借和债权转让
        结果：期望的结果和页面字符串可匹配
        :return:
        """
        exp1 = self.xml_read.r_data_hxb("test_loan_link_002", "expect_result1")
        exp2 = self.xml_read.r_data_hxb("test_loan_link_002","expect_result2")
        self.page.loan_link()
        actual = self.page.loan_link_res()

        assert actual[0] == exp1, "实际值:%s, 不等于%s" % (actual[0], exp1)
        assert actual[1] == exp2, "实际值:%s, 不等于%s" % (actual[1], exp1)


if __name__ == '__main__':
    pytest.main(['-vs', './test_hxb_home.py::TestHxbHome::test_plan_link_001'])