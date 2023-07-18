from selenium.webdriver.common.by import By
from elements.base_element import BaseElement
from utils.logger import Logger


class TextField(BaseElement):

    def __init__(self, element_by: By, element_locator: str, name: str):
        super().__init__(element_by, element_locator, name)

    def send_keys(self, text: str):
        Logger.info(f'Typing "{text}" in the {self.name}')
        self.wait_and_find_element().send_keys(text)

    def clear(self):
        Logger.info(f'Clearing the {self.name}')
        self.wait_and_find_element().clear()

    def get_text(self) -> str:
        Logger.info(f'Getting value from the {self.name}')
        return self.wait_and_find_element().get_attribute('value')
