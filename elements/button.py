from selenium.webdriver.common.by import By
from elements.base_element import BaseElement
from utils.logger import Logger


class Button(BaseElement):

    def __init__(self, element_by: By, element_locator: str, name: str):
        super().__init__(element_by, element_locator, name)

    def is_enabled(self) -> bool:
        Logger.info(f'Checking if {self.name} is enabled')
        return self.wait_and_find_element().is_enabled()
