
class Coin:

    def __init__(self, name, price, change):
        self.name = name
        self.price = price
        self.change = change

    def __str__(self):
        whiteSpaceName = "              "   
        whiteSpacePrice = "             "

        return "Name:{}{}\nPrice:{}{} usd\n24 hour % change:  {} %\n\n".format(whiteSpaceName, self.name, whiteSpacePrice, self.price, self.change)
