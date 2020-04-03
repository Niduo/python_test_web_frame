# coding = utf-8
"""
by: 老屋
des: 百度搜索demo
"""
from readConfig import ReadConfig
from common import browserType
from page.bdPage import BaiduPage
from common.readxml import Readxml
import pytest
import time


class TestBaidu:
    @classmethod
    def setup_class(cls):
        # driver = ReadConfig().driver_type
        cls.bd_url = ReadConfig().url_bd()
        cls.wd = browserType.browser("Chrome")
        cls.read_xml = Readxml()

    @classmethod
    def teardown_class(cls):
        browserType.browser_close()

    def setup(self):
        print('test method start!')

    def teardown(self):
        print('test method end!')

    def test_001(self):
        """
        描述：搜素python
        步骤：
        1、定位输入框
        2、输入字符python
        3、点击百度一下
        结果：python包括在结果内容中
        :return:
        """
        # 读取输入的关键字和期望结果
        word = self.read_xml.r_data_baidu("test_001_search_key", "words")
        expect_result = self.read_xml.r_data_baidu("test_001_search_key", "expect_result")
        # 调取封装的page方法
        page = BaiduPage(self.wd)
        page.open_(self.bd_url)
        time.sleep(2)
        page.search_key(word)
        time.sleep(2)
        assert expect_result in self.wd.page_source


if __name__ == '__main__':
    pytest.main(['-vs', 'TestBaidu'])





