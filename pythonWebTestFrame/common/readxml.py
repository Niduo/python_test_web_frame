from xml.dom import minidom
from readConfig import ReadConfig


class Readxml:
    def r_data_baidu(self, first_node, second_node):
        file_path = ReadConfig().data_baidu_file()
        file = minidom.parse(file_path)
        one_node = file.getElementsByTagName(first_node)[0]
        # 获取文件的二级标签
        two_node = one_node.getElementsByTagName(second_node)[0].childNodes[0].nodeValue
        return two_node

    def r_data_hxb(self, first_node, second_node):
        file_path = ReadConfig().data_hxb_file()
        file = minidom.parse(file_path)
        one_node = file.getElementsByTagName(first_node)[0]
        two_node = one_node.getElementsByTagName(second_node)[0].childNodes[0].nodeValue
        return two_node
