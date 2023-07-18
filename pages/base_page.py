from utils.logger import Logger


class BasePage:

    def __init__(self, unique_element, name: str):
        self._unique_element = unique_element
        self._name = name

    def is_loaded(self) -> bool:
        Logger.info(f'Checking if {self._name} is displayed')
        return self._unique_element.is_displayed()
