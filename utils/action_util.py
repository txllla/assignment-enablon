from selenium.webdriver import ActionChains

from utils.driver_util import DriverUtil


class ActionUtil:
    @staticmethod
    def move_to_element(element):
        actions = ActionChains(DriverUtil.get_instance())
        actions \
            .move_to_element(element) \
            .perform()

    @staticmethod
    def move_to_element_and_click(element):
        actions = ActionChains(DriverUtil.get_instance())
        actions \
            .move_to_element(element) \
            .click(element) \
            .perform()

    @staticmethod
    def double_click(element):
        actions = ActionChains(DriverUtil.get_instance())
        actions.double_click(element).perform()
