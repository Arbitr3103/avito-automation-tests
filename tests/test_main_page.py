from pages.main_page import MainPage


def test_main_page(browser):
    main_page = MainPage(browser, "https://www.avito.ru")
    main_page.open()
    assert main_page.is_search_bar_present(), "Search bar is not present"
