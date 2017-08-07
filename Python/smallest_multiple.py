def small():
    found = False
    count = 200
    while not found:
        count += 20
        if all(count%i == 0 for i in range (1,10)):
            print (count)
            found = True
        else:
            print (count)

small()