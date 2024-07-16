
from read import open_files, Laptops_display, user_option
from operation import *
from write import billing, update_file
import datetime


def user_option():
    print("\n")
    print("What can we help you with??")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    print("Press 1 for purchasing a laptop")
    print("Press 2 for selling a laptop")
    print("Press 3 for exiting the system")
    print("\n")


def exit_program():
    print("Thank you for using the system.")
    print("\n")


def project(my_dictionary,laptop_id):

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
            purchase_from_customer(my_dictionary,laptop_id)
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
        answer = input("Do you want to buy/sell another laptop? (Y/N): ").upper()
        print("\n")
        if answer == 'Y':
            user_option()
            laptop_id = get_laptop_id()
            project(my_dictionary, laptop_id)
            break
        elif answer == 'N':
            exit_program()
            break
        else:
            print("Invalid input. Please enter Y for yes or N for no")
            print("\n")


def get_laptop_id():
    while True:
        try:
            laptop_id = int(input("Please enter the laptop ID: "))
            return laptop_id
        except ValueError:
            print("Invalid input. Please enter a valid laptop ID.")


if __name__ == "__main__":
    my_dictionary = open_files()
    user_option()
    laptop_id = get_laptop_id()
    project(my_dictionary, laptop_id)