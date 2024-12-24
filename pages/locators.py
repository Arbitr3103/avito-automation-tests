from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = None
    CATEGORY_BUTTON = (By.XPATH, '//*[@id="app"]/div/buyer-location/div/div/div[2]/div/div[1]/div/div/div[3]/div[1]/div/div/div[1]/div[1]/div[1]/button')
    SEARCH_BAR = (By.CSS_SELECTOR, "input.styles-module-input-rA1dB")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="app"]/div/buyer-location/div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div[2]/button')
    RESULT_ITEMS = (By.XPATH, '//*[@id="app"]/div/buyer-location/div/div/div[2]/div/div[2]/div[2]/div/span')
