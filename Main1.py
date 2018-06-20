import datetime
import sys
import random
from pathlib import Path

from SecondSection.CMDShop import First

stock = First.order()


# for each in stock:
#     print(each)
def display_product(names):
    print("{} product are : ".format(names))
    for products in stock:
        print("Name : {}".format(products[0]))


product_name = []
max_row = len(stock)
# print(max_row)
display_product("Our")
is_found = False
updated_product_number = 0
price_of_product = 0
name = ""

# user_name = input("Enter your name ")
# print("Welcome to the shop : {}".format(user_name))

yes_or_no_option = input("Do you want to start the shopping? Y or N").lower()
while yes_or_no_option == "y":
    row = 0
    num = 0
    name = input("Enter your product Name : ")
    product_name.append(name)

    while row < max_row:
        if product_name[num] == stock[row][0]:
            is_found = True
            print("Your product found.")
            break
        else:

            row = row + 1
    num = num + 1

    if not is_found:
        print("We are exiting.")
        sys.exit(0)

    number_of_items = int(input("Enter the number of product you want to buy ? "))
    if stock[row][2] == "0":
        print("We are out of product")
    elif number_of_items > int(stock[row][2]):
        print("We have only {} items here....\nWant to reduce the number of product".format(stock[row][2]))
        yes_or_no = input("Yes or no").lower()
        if yes_or_no == "yes":
            new_product_number = int(input("Enter your product number"))
            if new_product_number < int(stock[row][2]):
                updated_product_number = int(stock[row][2]) - new_product_number
                price_of_product = int(stock[row][1]) * number_of_items
                stock[row][2] = str(updated_product_number)
                display_product("Other")
                yes_or_no_option = input("Do you want to want to shop again? Y or N")
            else:
                print("We are again out of number in this product")
        else:
            print("Ok, Continue then.")
    else:
        updated_product_number = (int(stock[row][2]) - number_of_items)
        stock[row][2] = str(updated_product_number)
        price_of_product = int(stock[row][1]) * number_of_items
        yes_or_no_option = input("Do you want to want to shop again? Y or N")
if yes_or_no_option == "n":
    modes = "w+"
    my_file = Path("Print.txt")
    if my_file.is_file():
        modes = "a"
    with open("Print.txt", modes) as print_text:
        for i in product_name:
            print("Date of purchase: {0}\nThe code of this product is : {1}\nPrice of product {2}".format(
                datetime.datetime.now(), random.randint(1, 1000), price_of_product), file=print_text)
            print("Name  {}".format(i), file=print_text)
