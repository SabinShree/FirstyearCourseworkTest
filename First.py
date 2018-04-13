def order():
    print("Available products are:")
    file = open("Stock.txt", "r")
    s = file.readlines()
    file.close()
    l = []
    for each in s:
        l.append(each.replace("\n", "").split(","))
    return l
