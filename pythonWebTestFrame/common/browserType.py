"""
by: 老屋
des: driver封装定义
"""

from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options

driver = None

# 启动浏览器
def browser(driver_type):

    """
    全局定义浏览器驱动
    :return:
    """
    global driver
    if driver_type == "Chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        # driver.set_window_size(1920, 1080)

    elif driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        # driver.set_window_size(1920, 1080)

    elif driver_type == "chrome-headless":
        # chrome headless模式 : 可以在后台运行浏览器
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif driver_type == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://10.2.16.182:4444/wd/hub',
                        desired_capabilities={
                              "browserName": "chrome",
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")
    return driver

# 关闭浏览器
def browser_close():
    global driver
    # yield driver
    driver.quit()