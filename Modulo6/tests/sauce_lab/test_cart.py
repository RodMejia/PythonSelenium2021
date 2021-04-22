from Modulo6.src.elements.cart_item import CartItem
from Modulo6.src.pages.cart import CartPage
from Modulo6.src.pages.login import LoginPage
from Modulo6.tests.common.test_base import TestBase


_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

_DEF_CART = 'YOUR CART'


class TestCart(TestBase):

    def test_cart_label(self):
        '''Adding article to cart and test if we're in the cart page and the item was the one we selected'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        inventory_page.header.goto_cart()
        cart = CartPage(self.driver)
        if cart.get_label() == _DEF_CART:
            print(f'User is in the Cart Page')
        item = cart.products[0]
        item: CartItem
        print(f'Product is {item.get_title()}')


    def test_go_back_from_cart(self):
        '''navigate to the Cart page and return to the catalog using the continue shopping button'''
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.header.goto_cart()
        cart = CartPage(self.driver)
        if cart.get_label() == _DEF_CART:
            print(f'User is in the Cart Page')
        inventory_ret = cart.go_back()
        print(f'{inventory_ret.get_label()}')


    def test_go_to_checkout(self):
        '''select an element and move to checkout'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        inventory_page.header.goto_cart()
        cart = CartPage(self.driver)
        cart.check_out()

