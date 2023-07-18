from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils.config_util import ConfigUtil
from utils.driver_util import DriverUtil
from utils.logger import Logger


class BaseElement:

    def __init__(self, element_by: By, element_locator: str, name: str):
        self._element_by = element_by
        self._element_locator = element_locator
        self.name = name

    def click(self):
        Logger.info(f'Clicking the {self.name}')
        self.wait_and_find_element().click()

    def get_text(self) -> str:
        Logger.info(f'Getting text from the {self.name}')
        return self.wait_and_find_element().text

    def is_displayed(self) -> bool:
        Logger.info(f'Checking if {self.name} is displayed')
        try:
            self.wait_and_find_element()
        except NoSuchElementException:
            return False
        return True

    def get_count_of_elements(self) -> int:
        Logger.info(f'Counting number of {self.name}s')
        return len(self.find_elements())

    def find_element(self) -> WebElement:
        return DriverUtil.get_instance().find_element(self._element_by, self._element_locator)

    def find_elements(self) -> List[WebElement]:
        return DriverUtil.get_instance().find_elements(self._element_by, self._element_locator)

    def wait_and_find_element(self) -> WebElement:
        return WebDriverWait(DriverUtil.get_instance(), ConfigUtil.get_webdriver_config()["wait-time"])\
            .until(ec.visibility_of_element_located((self._element_by, self._element_locator)))
