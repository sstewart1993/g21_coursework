import unittest
from src.pub import Pub
from src.customer  import Customer 
from src.drink import Drink 

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub('The Prancing Pony', 100.00)
        self.drink = Drink("Beer", 5.00, 6)
        self.customer = Customer("TJ", 50.00, 21)

    def test_pub_has_name(self):
        pub_name = self.pub.name
        self.assertEqual('The Prancing Pony', pub_name)

    def test_pub_has_till(self):
        pub_till = self.pub.till
        self.assertEqual(100.00, pub_till)

    def test_drink_count(self):
        count = self.pub.drinks
        self.assertEqual(0, len(count))

    def test_add_to_till(self):
        self.pub.add_to_till(self.drink)
        self.assertEqual(105.00, self.pub.till)

    def test_check_age(self):
        check = self.pub.check_age(self.customer)
        self.assertEqual('What can I get you?', check)

    def test_check_drunkenness_okay(self):
        check = self.pub.check_drunkenness(self.customer)
        self.assertEqual("Yeehaw", check)
    
    def test_check_drunkenness_too_drunk(self):
        self.customer.buy_drink(self.drink)
        check = self.pub.check_drunkenness(self.customer)
        self.assertEqual("You've had enough.", check)
    

