from Modulo6.src.elements.inventory_item import InventoryItem
from Modulo6.src.pages.login import LoginPage
from Modulo6.tests.common.test_base import TestBase
from Modulo6.src.pages.inventory import InventorySortOptions

_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

class TestInventoryDetails(TestBase):

    def test_inventory_details(self):
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        print(f'Title: {details_page.get_title()}')
        print(f'Description: {details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')
        details_page.add_to_cart()
        print(f'Total elements in cart: {details_page.header.get_total_cart_items()}')
        details_page.remove_from_cart()
        details_page.back()
        inventory_page.products.reload()
        assert len(inventory_page.products) == 6, 'Inventory len should be 6'

    def test_go_back_menu(self):
        '''go back to the catalog using the side menu'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.menu.open_menu()
        details_page.menu.back_to_inventory()
        inventory_page.products.reload()
        assert len(inventory_page.products) == 6, 'Inventory len should be 6'

    def test_add_article_details(self):
        '''adding article from the details page'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.add_to_cart()
        details_page.header.goto_cart()

    def test_add_article_details(self):
        '''adding article from the details page'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.add_to_cart()
        if details_page.header.get_total_cart_items():
            print(f'Article has been added to the cart')


    def test_remove_article_details(self):
        '''removing article from the details page'''
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.add_to_cart()
        details_page.remove_from_cart()
        if details_page.header.get_total_cart_items() == 0:
            print(f'Article was added and removed from the cart')
