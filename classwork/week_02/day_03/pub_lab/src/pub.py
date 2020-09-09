class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def drink_count(self):
        return len(self.drinks)

    def add_to_till(self, drink):
        self.till += drink.price

    def check_age(self, customer):
        if customer.age >= 18:
            return 'What can I get you?'
        else:
            return 'Get outta here kid!'

    def check_drunkenness(self, customer):
        if customer.drunkenness > 5:
            return "You've had enough."
        else:     
            return "Yeehaw"
