
class Coin:

    def __init__(self, name, price, change):
        self.name = name
        self.price = price
        self.change = change

    def __str__(self):
        whiteSpaceName = "              "   
        whiteSpacePrice = "             "

        return f"Name:{whiteSpaceName}{self.name}\nPrice:{whiteSpacePrice}{self.price} usd\n24 hour % change:  {self.change} %\n\n"
