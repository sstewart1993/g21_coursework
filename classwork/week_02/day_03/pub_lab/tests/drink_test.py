import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Beer", 5.00, 1)

    def test_drink_has_name(self):
        drink_name = self.drink.name
        self.assertEqual("Beer", drink_name)

    def test_drink_has_price(self):
        drink_price = self.drink.price
        self.assertEqual(5.00, drink_price)

    def test_drink_level(self):
        drink_level = self.drink.level
        self.assertEqual(1, drink_level)