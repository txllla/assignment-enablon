from selenium.webdriver.common.by import By
from elements.base_element import BaseElement
from utils.logger import Logger


class Checkbox(BaseElement):

    def __init__(self, element_by: By, element_locator: str, name: str):
        super().__init__(element_by, element_locator, name)
