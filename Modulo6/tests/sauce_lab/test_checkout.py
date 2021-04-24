from Modulo6.src.elements.checkout_item import CheckOutElements
from Modulo6.src.pages.cart import CartPage
from Modulo6.src.pages.checkout import CheckFormPage
from Modulo6.src.pages.login import LoginPage
from Modulo6.tests.common.test_base import TestBase


_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

_DEF_FNAME = 'rod'

_DEF_LNAME = 'mejia'

_DEF_CODE = '28765'

ERROR_MSG = 'Error: First Name is required'


class TestChkOut(TestBase):

    def test_chk_out(self):
        '''Test if we are in the Checkout page'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        inventory_page.header.goto_cart()
        cart = CartPage(self.driver)
        cart.check_out()
        chk = CheckFormPage(self.driver)
        print(f'{chk.get_label()}')

    def test_enter_info(self):
        '''Enter user info and click on Continue button'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        inventory_page.header.goto_cart()
        cart = CartPage(self.driver)
        cart.check_out()
        chk = CheckFormPage(self.driver)
        print(f'{chk.get_label()}')
        chk.login(_DEF_FNAME, _DEF_LNAME, _DEF_CODE)
        chk.cont_btn()

    def test_return_to_cart(self):
        '''verify the user can go back to the Cart page'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        inventory_page.header.goto_cart()
        cart = CartPage(self.driver)
        cart.check_out()
        chk = CheckFormPage(self.driver)
        cart_ret=chk.cancel()
        print(f'{cart_ret.get_label()}')


    def test_no_user_data(self):
        '''test an error message is displayed if no info is entered'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        inventory_page.header.goto_cart()
        cart = CartPage(self.driver)
        cart.check_out()
        chk = CheckFormPage(self.driver)
        chk.cont_btn()
        error_msg = chk.get_error_message()
        assert error_msg is not None, 'Error message should be displayed for invalid login'
        assert error_msg == ERROR_MSG, f'Error message should be {ERROR_MSG}'
