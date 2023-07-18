import allure

from pages.todo_page import TodoPage
from utils.driver_util import DriverUtil
from utils.keys_util import KeysUtil


def add_new_todo(title: str):
    todo_page = TodoPage()

    with allure.step("Create new todo"):
        with allure.step("Fill in title of todo"):
            todo_page.fill_in_new_todo_title(title)
            allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Press enter"):
            KeysUtil.press_enter()
            allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)


def edit_latest_todo(new_title: str):
    todo_page = TodoPage()

    with allure.step("Edit latest todo"):
        with allure.step("Double-click latest todo title"):
            todo_page.doubleclick_latest_todo_title()
            allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Enter new title"):
            todo_page.clear_and_fill_in_todo_edit_field_by_index(0, new_title)
            allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Press enter"):
            KeysUtil.press_enter()
            allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)


def delete_latest_todo():
    todo_page = TodoPage()

    with allure.step("Delete latest todo"):
        with allure.step("Click latest todo remove button"):
            allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                          name="before_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            todo_page.click_remove_latest_todo()
            allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                          name="after_screenshot",
                          attachment_type=allure.attachment_type.PNG)


def mark_latest_todo_completed():
    todo_page = TodoPage()

    with allure.step("Click checkbox in latest todo to mark it as completed"):
        allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                      name="before_screenshot",
                      attachment_type=allure.attachment_type.PNG)
        todo_page.click_latest_done_checkbox()
        allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                      name="after_screenshot",
                      attachment_type=allure.attachment_type.PNG)


def remove_completed_todos():
    todo_page = TodoPage()

    with allure.step("Click 'Clear completed' button"):
        allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                      name="before_screenshot",
                      attachment_type=allure.attachment_type.PNG)
        todo_page.click_clear_completed_button()
        allure.attach(DriverUtil.get_instance().get_screenshot_as_png(),
                      name="after_screenshot",
                      attachment_type=allure.attachment_type.PNG)


def check_latest_todo_is_completed():
    todo_page = TodoPage()

    with allure.step("Check latest todo is marked as completed"):
        assert todo_page.is_latest_todo_completed(), \
            "Latest todo is not marked as completed"


def check_number_of_todos_in_list_equals(number):
    todo_page = TodoPage()

    with allure.step(f'Check that number of todos displayed in the list is equal to {number}'):
        assert todo_page.get_number_of_todos_from_list() == number, \
            f'Expected count of todos to be equal "{number}"' \
            f', but got "{todo_page.get_number_of_todos_from_list()}"'


def check_todo_title_by_index(index: int, title: str):
    todo_page = TodoPage()

    with allure.step(f'Check title of todo number {index+1}'):
        assert todo_page.get_todo_title_by_index(index) == title, \
            f'Expected title of the latest todo to be equal "{title}"' \
            f', but got "{todo_page.get_todo_title_by_index(index)}"'


def check_todo_title_not_equals_by_index(index: int, title: str):
    todo_page = TodoPage()

    with allure.step(f'Check title of todo number {index+1} is not {title}'):
        assert todo_page.get_todo_title_by_index(index) != title, \
            f'Title of the latest todo equals to "{title}"'


def check_latest_todo_title_equals(title: str):
    todo_page = TodoPage()

    with allure.step(f'Check that latest todo title is equal to {title}'):
        assert todo_page.get_latest_todo_title() == title, \
            f'Expected title of the latest todo to be equal "{title}"' \
            f', but got "{todo_page.get_latest_todo_title()}"'


def check_todo_counter_equals(count: int):
    todo_page = TodoPage()

    with allure.step(f'Check that count is equal to {count}'):
        assert todo_page.get_todo_count() == count, \
            f'Expected count of todos to be equal "{count}"' \
            f', but got "{todo_page.get_todo_count()}"'
