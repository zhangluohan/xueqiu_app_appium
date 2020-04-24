from appium import webdriver


class AppDriver:

    driver = None

    @classmethod
    def driver_start(cls):
        caps = {}
        caps["automationName"] = "UiAutomator2"
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        caps["adbExecTimeout"] = 900000

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        cls.driver.find_element_by_id("tv_agree").click()
        #对于可以直接进入activity的apk,可以第二次直接进入activityc测试
        '''
        
        '''
    @classmethod
    def driver_quit(cls):
        cls.driver.quit()