import unittest

class NoCoinException(Exception):
    pass

class NoElementsException(Exception):
    pass

class NoSugarException(Exception):
    pass


class CoffeeMachinePlus:
    def __init__(self):
        self.coins = 0
        self.sugar = 0
        self.sugar_level_seleted = 0
        self.resources = {
            'coffee': 0,
            'milk': 0,
            'tea': 0,
        }
        self.recipies = {
            'coffee_alone': {
                'coffee': 30,
            },
            'coffee_with_milk': {
                'coffee': 30,
                'milk': 20,
            },
            'coffee_alone_with_sugar': {
                'coffee': 30,
                'sugar': 10,
            },
            'coffee_double': {
                'coffee': 60,
            },
            'tea_simple': {
                'tea': 10,
            },
        }

    def insert_coin(self):
        self.coins += 1

    def suger_level(self, level):
        self.sugar_level_seleted = level

    def add_resource(self, type, amount):
        self.resources[type] += amount

    def add_sugar(self, amount):
        self.sugar += amount

    def get_product(self, product_type):
        if self.coins == 0:
            raise NoCoinException()
        product_recipe = self.recipies[product_type]
        for product in product_recipe.keys():
            if self.resources[product] < product_recipe[product]:
                raise NoElementsException('Missing {}'.format(product))
        if self.sugar < self.sugar_level_seleted * 3:
            raise NoSugarException()

        self.coins -= 1
        self.sugar -= self.sugar_level_seleted * 3
        for product in product_recipe.keys():
            self.resources[product] -= product_recipe[product]






class CoffeeMachine:
    def __init__(self):
        self.coins = 0
        self.coffee = 0
        self.sugar = 0

    def insert_coin(self):
        self.coins += 1

    def insert_coffee(self, coffee):
        self.coffee += coffee

    def insert_sugar(self, sugar):
        self.sugar += sugar

    def get_coffee(self):
        if self.coins == 0:
            raise NoCoinException('No hay monedas')
        if self.count_coffee_left() == 0:
            raise NoElementsException('No hay elementos')
        # DESCONTAR
        self.coffee -= 30
        self.sugar -= 5
        self.coins -= 1
        return True

    def count_coffee_left(self):
        count_coffee_because_coffee = self.coffee // 30
        count_coffee_because_sugar = self.sugar // 5
        return min(count_coffee_because_coffee, count_coffee_because_sugar)


