def test_open_avito(browser):
    browser.get("https://www.avito.ru")
    assert "Авито" in browser.title
