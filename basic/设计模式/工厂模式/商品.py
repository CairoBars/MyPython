#Author:Cairo Li
class Burger():
    name=""
    price=0.0
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class cheeseBurger(Burger):
    def __init__(self):
        self.name="cheese burger"
        self.price=10.0
class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0
#小吃部分
class Snack():
    name=""
    price=0.0
    type="SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class chips(Snack):
    def __init__(self):
        self.name="chicken wings"
        self.price=12.0
class chickenWings(Snack):
    def __int__(self):
        self.name="chicken wings"
        self.price=12.0
#饮料部分
class Beverage(object):
    name=""
    price=0.0
    type="BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class coke(Beverage):
    def __init__(self):
        self.name="coke"
        self.price=4.0
class mike(Beverage):
    def __init__(self):
        self.name="mile"
        self.price=5.0


