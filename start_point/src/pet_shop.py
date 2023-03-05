# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop_name):
    return shop_name ["name"]

def get_total_cash(total):
    return total["admin"]["total_cash"]

def add_or_remove_cash(shop, amount_to_add):
    shop["admin"]["total_cash"] += amount_to_add

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, pets_to_add):
    shop["admin"]["pets_sold"] += pets_to_add

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets = []

    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet) 
    return pets

def find_pet_by_name(shop, name):

    for pet_name in shop["pets"]:
        if pet_name["name"] == name:
            return pet_name
    
def remove_pet_by_name(shop, name_to_remove):
    
    for pet in shop["pets"]:
        if pet["name"] == name_to_remove:
             shop["pets"].remove(pet)

def add_pet_to_stock(shop, pet_to_add):
   shop["pets"].append(pet_to_add)

   return len(shop["pets"])

def get_customer_cash(customer1):
    return customer1["cash"]

# def remove_customer_cash(customer, cash_to_remove):
#     return customer["cash"] - cash_to_remove

def get_customer_pet_count(customer1):
    return len(customer1["pets"])

def add_pet_to_customer(customer, pet_to_add):
    customer["pets"].append(pet_to_add)
    return len(customer["pets"])

def customer_can_afford_pet(customer, cheapest_pet):
    if customer["cash"] >= cheapest_pet["price"]:
        return True
    else:
        return False