# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(setup):
    return setup["name"]

def get_total_cash(setup):
    return setup["admin"]["total_cash"]

def add_or_remove_cash(setup, amount):
    cash_before = get_total_cash(setup)
    total_cash = cash_before + amount
    return total_cash





 