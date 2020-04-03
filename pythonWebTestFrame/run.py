# coding=utf-8
"""
by: 老屋
des：
1、用例创建原则，测试文件名必须以“test_”开头，测试函数必须以“test”开头,测试类必须以Test开头。
2、运行方式：
  > python3 run_tests.py  (回归模式，生成HTML报告)
  > python3 run_tests.py -m debug  (调试模式)
"""
import os
import time
import logging
import pytest
import click
from readConfig import ReadConfig

# 读取配置信息做变量
r = ReadConfig()
BASE_DIR = r.BASE_DIR
REPORT_DIR = r.report_dir()
cases_path = r.case_paths()
max_fail = r.max_fail()
rerun = r.rerun()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def init_env(now_time):
    """
    初始化测试报告目录
    """
    os.mkdir(REPORT_DIR+now_time)
    # os.mkdir(REPORT_DIR + now_time + "/image")


@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):

    if m is None or m == "run":
        logger.info("回归模式，开始执行")
        now_time = time.strftime("%Y%m%d_%H%M%S")
        # 在当前report文件夹下加入时间文件夹和image文件夹
        init_env(now_time)
        html_report = os.path.join(REPORT_DIR, now_time, "report.html")
        xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
        # --self-contained-html 为了发邮件时不丢失css，加入此参数
        pytest.main(["-s", "-v", cases_path,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", max_fail,
                     "--reruns", rerun])
        logger.info("运行结束，生成测试报告")
    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()