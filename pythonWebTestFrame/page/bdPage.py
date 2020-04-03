from page.basePage import BasePage
"""
by: 老屋
des: 定位及操作baid首页元素
"""


class BaiduPage(BasePage):
    def search_key(self, word):
        self.by_id_("kw").send_keys(word)
        self.by_id_("su").click()
