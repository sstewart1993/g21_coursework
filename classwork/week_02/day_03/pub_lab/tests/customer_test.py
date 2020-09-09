import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("TJ", 50.00, 21)
        self.drink = Drink("Beer", 5.00, 1)

    def test_has_name(self):
        customer_name = self.customer.name
        self.assertEqual("TJ", customer_name)

    def test_has_wallet(self):
        customer_wallet = self.customer.wallet
        self.assertEqual(50.00, customer_wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(45.00, self.customer.wallet)

    def test_drunkenness(self):
        customer_drunkenness = self.customer.drunkenness
        self.assertEqual(0, customer_drunkenness)
        
