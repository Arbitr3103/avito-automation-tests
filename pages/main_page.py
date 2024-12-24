from selenium.common import TimeoutException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.wait_for_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def is_search_bar_present(self):
        return self.wait_for_element(*MainPageLocators.SEARCH_BAR) is not None

    def select_category(self):
        """Нажимает кнопку выбора категории."""
        category_button = self.wait_for_element(*MainPageLocators.CATEGORY_BUTTON)
        category_button.click()

    def enter_search_query(self, query):
        """Вводит текст в строку поиска."""
        search_bar = self.wait_for_element(*MainPageLocators.SEARCH_BAR)
        search_bar.clear()
        search_bar.send_keys(query)

    def click_search_button(self):
        """Нажимает кнопку поиска."""
        search_button = self.wait_for_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()

    def is_results_visible(self):
        """Проверяет, что блок с результатами видим."""
        try:
            WebDriverWait(self.browser, 20).until(
                visibility_of_element_located(MainPageLocators.RESULT_ITEMS)
            )
            return True
        except TimeoutException:
            return False



