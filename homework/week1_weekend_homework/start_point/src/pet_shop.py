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


def get_pets_by_breed(pet_shop, pet_breed):
    counter = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            counter.append(pet)
    return counter
            
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    pet = find_pet_by_name(pet_shop, pet_name)
    new_pets = pet_shop["pets"].remove(pet)
    return new_pets

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    return get_stock_count(pet_shop)

def get_customer_cash(customers):
    for customer in customers:
        return customers["cash"]

def remove_customer_cash(customers, amount):
    cash_before = get_customer_cash(customers)
    new_cash = cash_before - amount
    customers["cash"] = new_cash
    return get_customer_cash(customers)

def get_customer_pet_count(customers):
    for customer in customers:
        return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    for customer in customers:
        return customers["pets"].append(new_pet)

# ------ Optional

def customer_can_afford_pet(customers, new_pet):
    for customer in customers:    
        if customers["cash"] >= new_pet["price"]:
            return True
        else:
            return False 

# ------ Integration Tests
    









    
    






 