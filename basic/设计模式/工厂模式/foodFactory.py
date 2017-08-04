from . import 34商品
#Author:Cairo Li
class foodFactory():
    type=""
    def createFood(self,foodClass):
        print(self.type,"factory produce a instance")
        foodIns=foodClass()
        return foodIns

class buegerFactory(foodFactory):
        self.type="BURGER"

class snackFactory(foodFactory):
    def __init__(self):
        self.type="SNACK"

class beverageFactory(foodFactory):
    def __init__(self):
        self.type="BEVERAGE"

if __name__=="__main__":
    bueger_Factory=buegerFactory()
    snack_Factory=snackFactory()
    beverage_Factory=beverageFactory()
    cheese_burger=bueger_Factory.createFood(cheeseBurger)