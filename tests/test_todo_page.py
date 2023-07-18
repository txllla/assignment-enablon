import allure
import pytest

import tests.steps.todo_page_steps as todo_steps

from utils.config_util import ConfigUtil
from utils.random_util import RandomUtil


class TestTodoPage:

    @allure.title("Add new todo")
    def test_add_new_todo(self, driver, logger, navigate_todo_page, delete_todo):
        todo_title = RandomUtil.get_random_alpha_string(ConfigUtil.get_test_data()["todo-title-len"])
        todo_steps.add_new_todo(todo_title)
        todo_steps.check_latest_todo_title_equals(todo_title)

    @allure.title("Edit todo")
    def test_edit_todo(self, driver, logger, navigate_todo_page, add_todo, delete_todo):
        new_todo_title = RandomUtil.get_random_alpha_string(ConfigUtil.get_test_data()["todo-title-len"])
        todo_steps.edit_latest_todo(new_todo_title)
        todo_steps.check_latest_todo_title_equals(new_todo_title)

    @allure.title("Delete todo")
    def test_delete_todo(self, driver, logger, navigate_todo_page, add_todo):
        todo_steps.delete_latest_todo()
        todo_steps.check_number_of_todos_in_list_equals(0)

    @allure.title("Mark todo as completed")
    def test_mark_todo_as_completed(self, driver, logger, navigate_todo_page, add_todo, delete_todo):
        todo_steps.mark_latest_todo_completed()
        todo_steps.check_latest_todo_is_completed()

    @allure.title("Check todos counter after adding new todo")
    def test_counter_after_adding_new_todo(self, driver, logger, navigate_todo_page, delete_todo):
        todo_steps.add_new_todo(RandomUtil.get_random_alpha_string(ConfigUtil.get_test_data()["todo-title-len"]))
        todo_steps.check_todo_counter_equals(1)

    @allure.title("Clear completed todo")
    def test_clear_completed_todo(self, driver, logger, navigate_todo_page, add_and_complete_todo):
        todo_steps.remove_completed_todos()
        todo_steps.check_number_of_todos_in_list_equals(0)

    @allure.title("Add 2 todos with the same name")
    def test_add_2_todos_with_same_name(self, driver, logger, navigate_todo_page, delete_all_todos):
        todo_title = RandomUtil.get_random_alpha_string(ConfigUtil.get_test_data()["todo-title-len"])
        todo_steps.add_new_todo(todo_title)
        todo_steps.add_new_todo(todo_title)
        todo_steps.check_number_of_todos_in_list_equals(2)

    @allure.title("Edit todo when there are 2 todos with the same title")
    @pytest.mark.parametrize('add_n_same_name_todos', [2], indirect=True)
    def test_edit_todo_when_2_with_same_title(self, driver, logger, navigate_todo_page,
                                              add_n_same_name_todos,
                                              delete_all_todos):
        new_todo_title = RandomUtil.get_random_alpha_string(ConfigUtil.get_test_data()["todo-title-len"])
        todo_steps.edit_latest_todo(new_todo_title)
        todo_steps.check_latest_todo_title_equals(new_todo_title)
        todo_steps.check_todo_title_not_equals_by_index(1, new_todo_title)

    @allure.title("Delete todo when there are 2 todos with the same title")
    @pytest.mark.parametrize('add_n_same_name_todos', [2], indirect=True)
    def test_delete_todo_when_2_with_same_title(self, driver, logger, navigate_todo_page,
                                                add_n_same_name_todos,
                                                delete_todo):
        todo_steps.delete_latest_todo()
        todo_steps.check_number_of_todos_in_list_equals(1)

    @allure.title("Change todo title to empty string")
    def test_edit_todo_to_empty_str(self, driver, logger, navigate_todo_page, add_todo, delete_todo):
        todo_steps.edit_latest_todo('')
        todo_steps.check_number_of_todos_in_list_equals(1)
        todo_steps.check_latest_todo_title_equals('')
