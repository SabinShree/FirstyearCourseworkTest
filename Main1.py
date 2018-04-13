import First
import datetime
import random

num = 0
price = 0
stock = First.order()
for each in stock:
    print(each)
Product = []
Name = input("Enter name:")
Address = input("Enter address:")
ans = input("Do you want to buy ? (Y or N)\n")
while ans == "y":
    Product.append(input("Enter product:"))
    qt = int(input("How many do you want??\n"))
    row = 0
    while row < 5:
        if Product[num] == stock[row][0]:
            break
        else:
            row = row + 1
    num = num + 1

    dummy = int(stock[row][2])
    if stock[row][2] == "0":
        print("Sry we are short of product")
        ans = input("Do u want anything else??")
    elif dummy < qt:
        bts = input("Do u want to decrease quantity?(y for yes and n for no)\n")
        if bts == "y":
            qt = int(input("Enter  new quantity!!\n"))
            change = int(stock[row][2]) - qt
            stock[row][2] = str(change)
            price = price + qt * (int(stock[row][1]))
            print("Remaining products are given")
            for each in stock:
                print(each)
            ans = input("Do u again want to buy anything???(y for yes/n for no)!!\n")
    else:
        change = int(stock[row][2]) - qt
        stock[row][2] = str(change)
        price = price + qt * (int(stock[row][1]))
        print("Remaining products are given")
        for each in stock:
            print(each)
        ans = input("Do u again want to buy anything???(y for yes/n for no)!!\n")

if ans == "n":
    print("Thanks for visiting")
    file = open("Invoice.txt", "w")

    (datetime.datetime.now())

    (random.randint(1, 1000))
    file.write("=================================================================")
    file.write("\n")
    file.write("Invoice")
    file.write("\n")
    file.write("Your purchase was performed on date and time: " + str(datetime.datetime.now()))
    file.write("\n")
    file.write("Code of the bill: " + str(random.randint(1, 1000)) + "\n")
    file.write("Name:" + Name + "\n")
    file.write("Address:" + Address + "\n")
    file.write("Price without discount = " + str(price) + "\n")
    file.write("Discount % = 10% \n")
    priceWithDiscount = price - ((10 / 100) * price)
    file.write("Amount to be paid with discount " + str(priceWithDiscount) + "\n")
    file.write("Product bought are:\n")
    k = 1
    for each in Product:
        file.write(str(k) + ":" + each + "\n")
        k = k + 1

    file.close()
