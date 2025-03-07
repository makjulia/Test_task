from pages.main_page import SearchHelper, SeacrhLocators


def get_count_elements(iterable):
    return len(iterable)


def get_elem_with_max_len(iterable):
    return max(iterable, key=len)


def test_func(browser):
    main_page = SearchHelper(browser)
    main_page.open()

    main_page.enter_word(SeacrhLocators.LOCATOR_NAME, "Ivan")
    main_page.enter_word(SeacrhLocators.LOCATOR_PASSWORD, "123")
    main_page.scroll_page()

    main_page.click_on_the_button(SeacrhLocators.LOCATOR_CHECKBOX_1)
    main_page.click_on_the_button(SeacrhLocators.LOCATOR_CHECKBOX_2)
    main_page.click_on_the_button(SeacrhLocators.LOCATOR_RADIOBUTTON)
    main_page.scroll_page()

    main_page.click_on_the_button(SeacrhLocators.LOCATOR_LIST)
    main_page.click_on_the_button(SeacrhLocators.LOCATOR_LIST_VARIABLE)
    main_page.enter_word(SeacrhLocators.LOCATOR_MAIL, "Ivan@example.com")

    auto_list = main_page.check_tools(SeacrhLocators.LOCATOR_LIST_TOOLS)
    count_el = get_count_elements(auto_list)
    el_with_max_len = get_elem_with_max_len(auto_list)

    main_page.enter_word(SeacrhLocators.LOCATOR_MESSAGE, f'{count_el}\n{el_with_max_len}')

    main_page.click_on_the_button(SeacrhLocators.LOCATOR_BUTTON)

    assert count_el == 5
    assert el_with_max_len == "Katalon Studio"
