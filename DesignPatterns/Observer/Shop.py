from Observer import ShopOnserver
from Pen import Pen

class Shop(ShopOnserver):
    def __init__(self, shopName: str):
        self._shopName = shopName

    def update(self, pen: Pen):
        print("pen prize changed to ", pen.penPrize, ' in ', self._shopName)


