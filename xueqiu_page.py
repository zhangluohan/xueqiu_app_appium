from page.basepage import BasePage
from page.mine_page import MinePage


class XueQiuPage(BasePage):

    _mine_button = BasePage.by_xpath("//*[@index='3']")

    def goto_mine_page(self):

        self.find(self._mine_button).click()
        return MinePage()