from Modulo6.src.elements.inventory_item import InventoryItem
from Modulo6.src.pages.inventory import InventorySortOptions
from Modulo6.src.pages.login import LoginPage
from Modulo6.tests.common.test_base import TestBase


_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

VALID_PRICES = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']

VALID_LABELS = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt']


class TestInventory(TestBase):

    def test_prices(self):
        """Test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for index, item in enumerate(inventory.products):
            item: InventoryItem
            assert item.get_price() == VALID_PRICES[index], f'Price for item {index} should be {VALID_PRICES[index]}'
            print('\n')
            print(item.get_title())
            print(item.get_description())
            print(item.get_price())
            print('*' * 80)


    def test_label(self):
        """Test production label."""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        assert inventory.get_label() == 'PRODUCTS', 'Inventory page label should be Products'

    def test_sort(self):
        """Test sort products"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.get_sort_value() == InventorySortOptions.A_TO_Z.value, 'Default sort should be A to Z'
        for option in InventorySortOptions:
            inventory.sort_by(option)
            inventory.get_sort_value() == option.value, f'Default sort should be {option.value}'

    #------------------------------------------------------

    def test_btn(self):
        """test button label of a not added item"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        item = inventory.products[0]
        item: InventoryItem
        if item.is_not_the_cart():
            print(f'Item is not added to the cart')

    def test_click_to_add(self):
        '''adds the item to the cart and checks the label is updated to REMOVE'''
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        item = inventory.products[0]
        item: InventoryItem
        item.add_to_cart()
        if item.is_in_the_cart():
            print(f'The item was added to the cart')

    def test_menu(self):
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.menu.open_menu()
        inventory.menu.logout()


    def test_product1(self):
        """Test label"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        item = inventory.products[0]
        print(item.get_title())
        assert item.get_title() == VALID_LABELS[0], f'Label for item {0} should be {VALID_LABELS[0]}'





