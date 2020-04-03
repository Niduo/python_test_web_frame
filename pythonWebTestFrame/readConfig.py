# coding = utf-8
"""
by: 老屋
des: 封装读取配置文件config.txt属性
"""
import configparser
import os


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        # self.current = os.path.dirname(__file__)
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.cf.read(self.BASE_DIR+"./config.txt")

    def report_dir(self):
        value = self.BASE_DIR + self.cf.get("REPORT_DIR", "report_path")
        return value

    def driver_type(self):
        value = self.cf.get("BROWSER", "driver_type")
        return value

    def url_bd(self):
        value = self.cf.get("BROWSER", "url_bd")
        return value

    def url_hxb(self):
        value = self.cf.get("BROWSER", "url_hxb")
        return value

    def case_paths(self):
        value = self.cf.get("REPORT_DIR", "cases_path")
        return value

    def max_fail(self):
        value = self.cf.get("REPORT_DIR", "max_fail")
        return value

    def rerun(self):
        value = self.cf.get("REPORT_DIR", "rerun")
        return value

    def data_baidu_file(self):
        value = self.BASE_DIR+self.cf.get("RESOURCES", "baidu_file")
        return value

    def data_hxb_file(self):
        value = self.BASE_DIR+self.cf.get("RESOURCES", "hxb_file")
        return value

