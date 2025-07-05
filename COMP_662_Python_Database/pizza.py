import logging
logging.basicConfig(filename="test.log", level=logging.DEBUG)
#logging.basicConfig(filename="test.log", level=logging.DEBUG format="%(asctime)s:%(levelname)s:%(message)s")
class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("Pizza created: {} (${})".format(self.name, self.price))
        logging.debug("Pizza created: {} (${})".format(self.name, self.price))

    def make(self, quantity=1):
        print("Made {} {} pizza(s)".format(quantity, self.name))
        logging.debug("Made {} {} pizza(s)".format(quantity, self.name))

    def eat(self, quantity=1):
        print("Ate {} pizza(s)".format(quantity, self.name))
        logging.debug("Ate {} pizza(s)".format(quantity, self.name))

# Modify the parameters of the pizza_01 object
pizza_01 = Pizza("Sicilian", 18)
pizza_01.make(5)
pizza_01.eat(4)

# Modify the parameters of the pizza_02 object
pizza_02 = Pizza("quattro formaggi", 16)
pizza_02.make(2)
pizza_02.eat(2)