class Coin:

    def __init__(self, name, price, change):
        self.name = name
        self.price = price
        self.change = change

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def change(self):
        return self.__change

    @name.setter
    def name(self, name):
        if type(name) not in [str]:
            TypeError
        else:
            self.__name = name

    @price.setter
    def price(self, price):
        try:
            float(price)
            self.__price = price
        except:
            print("Price couldn't be converted to a number.")
            raise TypeError

    @change.setter
    def change(self, change):
        try:
            float(change)
            self.__change = change
        except:
            print("Change couldn't be converted to a number.")
            raise TypeError

    def __str__(self):
        whiteSpaceName = "              "   
        whiteSpacePrice = "             "

        return "Name:{}{}\nPrice:{}{} usd\n24 hour % change:  {} %\n\n".format(whiteSpaceName, str(self.__name), whiteSpacePrice, self.__price, self.__change)
