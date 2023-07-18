from selenium.webdriver.common.by import By

from elements.button import Button
from elements.checkbox import Checkbox
from elements.text import Text
from elements.text_field import TextField
from pages.base_page import BasePage
from utils.action_util import ActionUtil
from utils.logger import Logger


class TodoPage(BasePage):
    def __init__(self):
        super().__init__(TextField(By.XPATH, "//input[contains(@class, 'new-todo')]", "New Todo field"),
                         "Todo page")

        self.__todo_field = TextField(By.XPATH, "//input[contains(@class, 'new-todo')]", "New Todo field")
        self.__todo_count = Text(By.XPATH, "//span[@class='todo-count']", "Todo count")
        self.__todo_titles = Text(By.XPATH, "//ul[@class='todo-list']/li//label", "Todo titles")
        self.__clear_completed_button = Button(By.XPATH, "//button[@class='clear-completed']", "Clear completed button")

        self.__todo_done_checkbox_locator = "(//input[@class='toggle'])[{}]"
        self.__todo_locator = "//ul[@class='todo-list']/li[{}]"
        self.__todo_title_locator = "//ul[@class='todo-list']/li[{}]//label"
        self.__todo_edit_field_locator = "//ul[@class='todo-list']/li[{}]//input[@class='edit']"
        self.__todo_remove_button_locator = "//ul[@class='todo-list']/li[{}]//button[@class='destroy']"

    def fill_in_new_todo_title(self, text: str):
        self.__todo_field.send_keys(text)

    def get_latest_todo_title(self) -> str:
        return self.get_todo_title_by_index(0)

    def get_todo_title_by_index(self, index: int) -> str:
        Logger.info(f'Getting Todo title from Todo number {index+1}')
        todo_title = Text(By.XPATH,
                          self.__todo_title_locator.format(index + 1),
                          f'Todo number {index + 1} - Title')
        return todo_title.get_text()

    def get_number_of_todos_from_list(self) -> int:
        Logger.info("Getting number of Todos from the list")
        return self.__todo_titles.get_count_of_elements()

    def is_latest_todo_completed(self) -> bool:
        return self.is_todo_completed_by_index(0)

    def is_todo_completed_by_index(self, index: int) -> bool:
        Logger.info(f'Checking if Todo number {index + 1} is completed')
        todo = Text(By.XPATH,
                    self.__todo_locator.format(index + 1),
                    f'Todo number {index + 1}')
        if 'completed' in todo.wait_and_find_element().get_attribute('class').split():
            return True
        return False

    def doubleclick_latest_todo_title(self):
        self.doubleclick_todo_title_by_index(0)

    def doubleclick_todo_title_by_index(self, index: int):
        Logger.info(f'Double-clicking the Todo number {index + 1}')
        todo_title = Text(By.XPATH,
                          self.__todo_title_locator.format(index + 1),
                          f'Todo number {index + 1} - Title')
        ActionUtil.double_click(todo_title.wait_and_find_element())

    def clear_and_fill_in_todo_edit_field_by_index(self, index: int, text: str):
        edit_field = TextField(By.XPATH,
                               self.__todo_edit_field_locator.format(index + 1),
                               f'Todo edit field number {index + 1}')
        edit_field.clear()
        self.doubleclick_todo_title_by_index(index)
        edit_field.send_keys(text)

    def click_latest_done_checkbox(self):
        self.click_done_checkbox_by_index(0)

    def click_done_checkbox_by_index(self, index: int):
        Logger.info(f'Clicking "Done" checkbox in Todo number {index + 1}')
        todo_done_checkbox = Checkbox(By.XPATH,
                                      self.__todo_done_checkbox_locator.format(index + 1),
                                      f'Todo number {index + 1} - Done checkbox')
        todo_done_checkbox.find_element().click()

    def click_remove_latest_todo(self):
        self.click_remove_todo_by_index(0)

    def click_remove_todo_by_index(self, index: int):
        Logger.info(f'Clicking "X" button in Todo number {index + 1}')
        todo_title = Text(By.XPATH,
                          self.__todo_title_locator.format(index + 1),
                          f'Todo number {index + 1} - Title')
        todo_remove_button = Button(By.XPATH,
                                    self.__todo_remove_button_locator.format(index + 1),
                                    f'Todo number {index + 1} - Remove button')
        ActionUtil.move_to_element(todo_title.wait_and_find_element())
        ActionUtil.move_to_element_and_click(todo_remove_button.wait_and_find_element())

    def get_todo_count(self) -> int:
        Logger.info("Getting number of Todos from the counter")
        return int(self.__todo_count.get_text().split(" ")[0])

    def click_clear_completed_button(self):
        self.__clear_completed_button.click()
