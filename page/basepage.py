from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    _black_list=[
        (By.id, "user_profile_icon"),
    ]  #定位符
    _max = 0

    def __int__(self, driver: WebDriver):
        self.driver = driver      #todo:no AppDriver().

    def find(self, element_locator)-> WebElement:
        # 添加黑名单
        try:
            return self.driver.find_element(*element_locator)
        except Exception as e:
            if BasePage._max>3:
                raise e
            BasePage._max=BasePage._max+1
            for ele in self._black_list:
                elements = self.driver.find_elements(*ele)
                if len(elements)>=1:
                    elements[0].click()
            return self.find(element_locator)  #回调

    @classmethod
    def by_id(cls, value) -> tuple:
        tuple_t = (By.ID, value)
        return tuple_t

    @classmethod
    def by_xpath(cls, value) -> tuple:
        tuple_t = (By.XPATH, value)
        return tuple_t
