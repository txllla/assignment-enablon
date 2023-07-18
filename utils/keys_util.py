from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from utils.driver_util import DriverUtil


class KeysUtil:

    @staticmethod
    def press_enter():
        actions = ActionChains(DriverUtil.get_instance())
        actions.send_keys(Keys.ENTER).perform()
