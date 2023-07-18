import pytest

from pages.todo_page import TodoPage
from utils.config_util import ConfigUtil
from utils.keys_util import KeysUtil
from utils.logger import Logger
from utils.driver_util import DriverUtil
from utils.random_util import RandomUtil

TEST_URL = ConfigUtil.get_test_data()["test-url"]
TODO_PAGE = TEST_URL + ConfigUtil.get_test_data()["endpoints"]["to-do"]


@pytest.fixture
def driver():
    driver = DriverUtil.get_instance()
    yield driver
    DriverUtil.quit_and_reset()


@pytest.fixture
def logger():
    return Logger()


@pytest.fixture
def navigate_todo_page(driver):
    driver.get(TODO_PAGE)


@pytest.fixture
def add_todo(driver):
    todo_title = RandomUtil.get_random_alpha_string(ConfigUtil.get_test_data()["todo-title-len"])
    todo_page = TodoPage()
    todo_page.fill_in_new_todo_title(todo_title)
    KeysUtil.press_enter()


@pytest.fixture
def add_n_same_name_todos(request, driver):
    todo_title = RandomUtil.get_random_alpha_string(ConfigUtil.get_test_data()["todo-title-len"])
    todo_page = TodoPage()
    for i in range(request.param):
        todo_page.fill_in_new_todo_title(todo_title)
        KeysUtil.press_enter()


@pytest.fixture
def add_and_complete_todo(driver, add_todo):
    todo_page = TodoPage()
    todo_page.click_latest_done_checkbox()


@pytest.fixture
def delete_todo(driver):
    yield
    TodoPage().click_remove_latest_todo()


@pytest.fixture
def delete_all_todos(driver):
    todo_page = TodoPage()
    yield
    for i in range(todo_page.get_number_of_todos_from_list()):
        todo_page.click_remove_latest_todo()
