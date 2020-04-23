import pytest

from appdriver.app_driver import AppDriver

if __name__ == "__main__":

    AppDriver.driver_start()

    pytest.main(['testcase/test_login.py'])


    AppDriver.driver_quit()