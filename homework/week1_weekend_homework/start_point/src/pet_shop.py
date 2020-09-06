# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
     cash = get_total_cash(pet_shop)
     new_cash = cash + amount
     pet_shop["admin"]["total_cash"] = new_cash
     return get_total_cash(pet_shop)

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, new_sales):
    sold = get_pets_sold(pet_shop)
    new_sold = sold + new_sales
    pet_shop["admin"]["pets_sold"] = new_sold
    return get_pets_sold(pet_shop)

def get_stock_count(pet_shop):
    count = len(pet_shop["pets"])
    return count










    
    






 