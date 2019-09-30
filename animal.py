
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("{0} is eating.".format(self.name))
    def drink(self):
        print("{0} is drinking.".format(self.name))
