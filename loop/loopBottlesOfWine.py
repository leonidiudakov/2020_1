#prints the 99 bottle of wine on the wall classic

x = 99
while x >= 3:
    print(str(x) + " bottles of wine on the wall,")
    print(str(x) + " bottles of wine in all,")
    print("Take one, pass it around,")
    x = x - 1
    print("Now there are " + str(x) + " bottles of wine left.")

    
print("2 bottles of wine on the wall,")
print("2 bottles of wine in all,")
print("Take one, pass it around")
print("Now there is 1 bottle of wine left.")
print("1 bottle of wine on the wall,")
print("1 bottle of wine in all,")
print("Take one, pass it around")
print("Now there are no bottles of wine left.")
