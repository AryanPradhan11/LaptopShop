from main import *
from write import update_file, billing
import datetime
def user_input():
    while True:
        try:
            user_name = input("Enter User Name: ")
            print("\n")
            user_address = input("Enter User Address: ")
            print("\n")
            user_phone_number = int(input("Enter User Phone Number: "))
            print("\n")
            return user_name, user_address, user_phone_number
        except ValueError:
            print("Invalid Input. Please try again.")
def sales_to_customer(my_dictionary):
    user_name, user_address, user_phone_number = user_input()

    laptop_id = int(input(f"Hello, {user_name},Please enter the id of the product you would like to purchase : "))

    print("\n")

    while True:
        quantity = int(input(f"How many pieces of {my_dictionary[laptop_id][0]} would you like to buy? : "))
        print("\n")

        if quantity <= 0:
            print("Invalid Input. Please enter a valid quantity.")
            continue

        if int(my_dictionary[laptop_id][-1]) == 0:
            print("The product is sold")
            return

        if int(quantity) > int(my_dictionary[laptop_id][-1]):
            print(
                "The quantity of product you're trying to buy is currently unavailable. Please re-select the quantity")
        else:
            break

    update = int(my_dictionary[laptop_id][-1]) - int(quantity)

    update_file(laptop_id, update)

    details_laptop = my_dictionary[laptop_id]
    brand = details_laptop[1]
    price = details_laptop[4]

    subtotal = int(quantity) * int(price)
    tax = subtotal * 0.13
    total_price = subtotal + tax
    current_time = datetime.datetime.now()

    ship = input(("Would you like to ship your product?Please press Y as Yes and N if No: "))
    print("\n")

    shipping_cost = 0
    if (ship == "Y"):
        shipping = input(("Please press 1 for outside valley and press 2 for indoor valley: "))
        print("\n")
        if shipping == "1":
            shipping_cost == 20000
            print("Your shipping cost will be 20,000.")
            total_price += shipping_cost
            print("\n")

        elif shipping == "2":
            shipping_cost == 1000
            print("Your shipping cost will be 1000.")
            total_price += shipping_cost
            print("\n")

        else:
            print("Invalid shipping option. Please re-select")
            print("\n")

    elif ship == "N":
        print("The product will not be shipped.")
        print("\n")

    else:
        print("Invalid Option.")
        print(ship)

    try:
        bill_file = open("bill.txt", "w")
        bill_file.write(f"Bill Date: {current_time}\n")
        bill_file.write(f"Customer Name: {user_name}\n")
        bill_file.write(f"Customer Address: {user_address}\n")
        bill_file.write(f"Laptop Brand: {brand}\n")
        bill_file.write(f"Laptop Price: NRP{price}\n")
        bill_file.write(f"Quantity:{quantity}\n")
        bill_file.write(f"Tax: NRP{tax}\n")
        bill_file.write(f"Total Price: NRP{total_price}\n")
        billing(bill_file)
        bill_file.close()

    except IOError:
        print("Error generating bill")

    print("Thank you for the purchase. Visit Again.")
    print("\n")


def purchase_from_customer(my_dictionary, laptop_id):
    user_name, user_address, user_phone_number = user_input()
    while True:
        seller_product = input(f"{user_name} What is the product you are willing to sell us?: ")
        print("\n")
        seller_quantity = int(input(f"Enter the amount of {seller_product} to be sold: "))
        if seller_quantity <= 0:
            print("Invalid quantity. Quantity must be a positive value. Please re-enter.")
            continue
        print("\n")
        seller_model = input(f"Enter the brand name for {seller_product}: ")
        print("\n")
        seller_price = input("Enter the price: ")
        print("\n")
        seller_card = input("Enter the grraphics card: ")
        print("\n")
        seller_processor = input("Enter the processor: ")
        print("\n")
        break

    product_exists = False
    with open("laptop.txt", "r") as laptop_file:
        for line in laptop_file:
            if seller_product in line:
                product_exists = True
                # Split the line and extract the quantity
                quantity = int(line.split(",")[-1])
                if quantity<=0:
                    continue
                break

    if product_exists:
        seller_quantity = input(f"Enter the additional amount of {seller_product} to be sold: ")
        new_quantity = int(seller_quantity) + quantity
    else:
        seller_quantity = input(f"Enter the amount of {seller_product} to be sold: ")
        new_quantity = int(seller_quantity)

    seller_details = f"{seller_product}, {seller_model},{seller_processor},{seller_card},{seller_price},{seller_quantity}\n"

    with open("laptop.txt", "a") as laptop_files:
        laptop_files.write(seller_details)

    total_price = 0  # Initialize the total_price variable

    print("Thank you for the product. Visit Again!!!")
    print("\n")

    time = datetime.datetime.now()

    # Generate bills for this function
    billing_file = open("billing.txt", "a")
    billing_file.write(f"Bill Date: {time}\n")
    billing_file.write(f"Seller Name: {user_name}")


def exit_program():
    print("Thank you for using the system.")
    print("\n")


def project(my_dictionary):
    while True:
        user_input = int(input("Enter an option: "))

        if user_input == 1:
            if my_dictionary.get(laptop_id):
                sales_to_customer(my_dictionary)
                print("\n")
                another()
                break
            else:
                print("Please enter valid laptop id")
                continue

        elif user_input == 2:
            purchase_from_customer(my_dictionary, laptop_id)
            print("\n")
            another()
            break

        elif user_input == 3:
            exit_program()
            print("\n")
            break

        else:
            print("The option is invaild. Please select an option between 1, 2 or 3")
            print("\n")


def another():
    while True:
        answer = input("Do you want to buy/sell another laptop?: ").upper()
        print("\n")
        if answer == 'Y':
            user_option()
            project(my_dictionary)
            break
        elif answer == 'N':
            exit_program()
            break
        else:
            print("Invalid input. Please enter Y for yes or N for no")
            print("\n")


def update_file(laptop_id, update):
    file_laptops = open("laptop.txt", "r")
    lines = file_laptops.readlines()
    file_laptops.close()

    lines[laptop_id - 1] = lines[laptop_id - 1].rstrip()  # Remove the newline character
    lines[laptop_id - 1] = lines[laptop_id - 1].rsplit(",", 1)[0] + ", " + str(update) + "\n"

    file_laptops = open("laptop.txt", "w")
    file_laptops.writelines(lines)
    file_laptops.close()