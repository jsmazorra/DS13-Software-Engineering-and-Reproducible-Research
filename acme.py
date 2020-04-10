import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        x = self.price / self.weight
        if x < 0.5:
            return "Not so stealable..."
        elif x < 1.0:
            return "Kinda stealable"
        else:
            return "Very stealable!"

    def explode(self):
        y = self.flammability * self.weight
        if y < 10:
            return "...fizzle."
        elif y < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name):
        super().__init__(name)
        self.weight = 10

    def explode(self):
        return "...it's a glove."

    def punch(self):
        power = self.weight
        if power < 5:
            return "That tickles."
        elif power < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
