import datetime

def open_files():
    file_laptops = open("laptop.txt", "r")
    my_dictionary={}
    laptop_id = 1
    for i in file_laptops:
        i = i.replace("\n","")
        my_dictionary.update({laptop_id:i.split(",")})
        laptop_id +=1
        print(i)
    file_laptops.readlines()
    file_laptops.close()
    return my_dictionary

def Laptops_display():
    print("\t\t\t\t\t\t <-------------------- Welcome to our shop -------------------->")
    print("\t\t\t\t------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Laptop ID    Laptop Brand  Model   Processor  Graphics  Price  Quantity")


    file = open("laptop.txt", "r")
    a = 1

    for product in file:
        print(" ",a,"           ",product.replace("," , ""))
        a = a+1

    file.close()
Laptops_display()


def user_option():
    print("\n")
    print("What can we help you with??")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    print("Press 1 for purchasing a laptop")
    print("Press 2 for selling a laptop")
    print("Press 3 for exiting a system")
    print("\n")