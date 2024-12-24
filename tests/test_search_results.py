from pages.main_page import MainPage


def test_search_results(browser):
    main_page = MainPage(browser, "https://www.avito.ru")
    main_page.open()
    main_page.enter_search_query("Ноутбук")
    main_page.click_search_button()
    assert main_page.is_results_visible(), "Search results are not displayed."
