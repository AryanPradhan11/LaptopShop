def validate_laptop_id(laptop_id, my_dictionary):
    return laptop_id in my_dictionary

def validate_quantity(quantity, laptop_id, my_dictionary):
    quantity = int(quantity)
    if laptop_id in my_dictionary:
        available_quantity = int(my_dictionary[laptop_id][-1])
        return quantity <= available_quantity
    return False

def validate_name(name):
    return name.isalpha()

def validate_phone_number(phone_number):
    return phone_number.isdigit()