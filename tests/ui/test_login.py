import pytest
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage

def test_successful_login(page):
    # initialise page objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # navigate and log in
    login_page.navigate()
    # Swag Labs provides 'standard_user' as a valid test account
    login_page.login("standard_user", "secret_sauce")

    # vrify we reached the inventory page
    assert inventory_page.is_loaded() is True
    assert inventory_page.get_item_count() > 0

def test_locked_out_user_login(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    #verify the correct error message appears
    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert login_page.get_error_message() == expected_error