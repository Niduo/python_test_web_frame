web测试demo

###################################################

框架结构说明：
数据驱动模式，将程序和数据分离，便于代码的维护，page object封装在BasePage，页面元素在*page.py中维护，入参和期望结果在xml中维护
python+pytest+selenium+pageObject

package dir：
common  封装xml读取，driver封装
page 封装page基准类，以及每个页面元素定位的编写
resources 存放读取结果，以及数据数据
test_report 存放测试报告
test_dir 测试用例
config.txt 存放全局变量的参数
readConfig.py 读取配置文件config.txt

###################################################
