
class InventoryItemMixin:
    __ADDED_LABEL = 'ADD TO CART'

    __REMOVE_LABEL = 'REMOVE'

    def get_title(self):
        return self._title.get_text()


    def get_description(self):
        return self._description.get_text()


    def get_price(self):
        return self._price.get_text()


    def is_not_the_cart(self):
        return self._inv_btn.get_text() == InventoryItemMixin.__ADDED_LABEL

    def is_in_the_cart(self):
        return self._inv_btn.get_text() == InventoryItemMixin.__REMOVE_LABEL


    def add_to_cart(self):
        if self._inv_btn.get_text() == InventoryItemMixin.__ADDED_LABEL:
            self._inv_btn.click()
        else:
             raise ValueError(f'Inventory item is already in the cart')


    def remove_from_cart(self):
        if self._inv_btn.get_text() == InventoryItemMixin.__REMOVE_LABEL:
            self._inv_btn.click()
        else:
            raise ValueError(f'Inventory item is not in the cart')