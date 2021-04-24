from Modulo6.src.elements.overview_item import OverviewItem
from Modulo6.src.elements.overview_items import OverviewItems
from Modulo6.src.pages.cart import CartPage
from Modulo6.src.pages.checkout import CheckFormPage
from Modulo6.src.pages.login import LoginPage
from Modulo6.src.pages.overview import Overview
from Modulo6.src.pages.inventory import InventoryItems
from Modulo6.tests.common.test_base import TestBase
from Modulo6.src.elements.cart_item import CartItem


_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

_DEF_FNAME = 'rod'

_DEF_LNAME = 'mejia'

_DEF_CODE = '28765'

_TOTAL = '$49.66'

class TestOverview(TestBase):

    def test_get_to_overview(self):
        '''verify the user is in the Overview page'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item.add_to_cart()
        inventory_page.header.goto_cart()
        cart = CartPage(self.driver)
        cart.check_out()
        chk = CheckFormPage(self.driver)
        print(f'{chk.get_label()}')
        chk.login(_DEF_FNAME, _DEF_LNAME, _DEF_CODE)
        chk.cont_btn()
        over = Overview(self.driver)
        print(f'{over.get_page_label()}')

    def test_totals(self):
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        second_item = inventory_page.products[2]
        first_item.add_to_cart()
        second_item.add_to_cart()
        inventory_page.header.goto_cart()
        cart = CartPage(self.driver)
        cart.check_out()
        chk = CheckFormPage(self.driver)
        chk.login(_DEF_FNAME, _DEF_LNAME, _DEF_CODE)
        chk.cont_btn()
        over = Overview(self.driver)
        assert over.get_total() == _TOTAL, f'Total should be {_TOTAL}'