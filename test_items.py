import pytest
from selenium import webdriver


def test_add_to_basket_button_is_visiable(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        browser.implicitly_wait(5)
        button = browser.find_element_by_css_selector('.btn-add-to-basket')
        assert button.is_displayed() == True, "Button 'Add to basket' is absent"




