import datetime

def billing(content):
    with open("bill.txt", "a") as bill_file:
        bill_file.write(str(content))

def update_file(laptop_id, update):
    file_laptops = open("laptop.txt", "r")
    lines = file_laptops.readlines()
    file_laptops.close()

    lines[laptop_id - 1] = lines[laptop_id - 1].rstrip()  # Remove the newline character
    lines[laptop_id - 1] = lines[laptop_id - 1].rsplit(",", 1)[0] + ", " + str(update) + "\n"

    file_laptops = open("laptop.txt", "w")
    file_laptops.writelines(lines)
    file_laptops.close()