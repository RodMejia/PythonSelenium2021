

class OverviewItemMixin:

    def get_title(self):
        return self._title.get_text()


    def get_description(self):
        return self._description.get_text()


    def get_price(self):
        return self._price.get_text()



