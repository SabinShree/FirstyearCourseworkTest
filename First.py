def order():
    my_list = []
    with open("Stock.txt", "r") as my_file:
        new_file = my_file.readlines()
        for line in new_file:
            my_list.append(line.strip("\n").split(","))
    return my_list

# print(order())
