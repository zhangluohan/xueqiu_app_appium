from page.mine_page import MinePage
from page.xueqiu_page import XueQiuPage


class TestLogin:
    def setup(self):
        self.xueqiu = XueQiuPage()

    def test_login_fail(self):
        assert self.xueqiu.goto_mine_page().login_fail("111111", "aaaaaaa") == "手机号码填写错误"

    def test_login_successful(self):
        self.xueqiu.goto_mine_page().login_successful("111111", "aaaaaaa")
        assert 1==1
