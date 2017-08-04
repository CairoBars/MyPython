#Author:Cairo Li
from ..单利模式 import 商品
class order():
    burger=""
    snack=""
    beverage=""
    def __init__(self,orderBuilder):
        self.burger=orderBuilder.bBurger
        self.snack=orderBuilder.bSnack
        self.beverage=orderBuilder.bBeverage

class orderBuilder():
    bBurger=""
    bSnack=""
    bBeverage=""
    def addBurger(self,xBurger):
        self.bBurger=xBurger
    def addSnack(self,xSnack):
        self.bSnack=xSnack
    def addBeverage(self,xBeverage):
        self.bBeverage=xBeverage
    def build(self):
        return order()