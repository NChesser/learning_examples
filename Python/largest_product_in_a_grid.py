

def product_grid():
    with open('series2.txt') as f:
        numbers = f.read().splitlines()
    

    for i, line in enumerate(numbers):
        #num = line.split()
        for n in line:
            print(n)
            #print(down(i, int(n), numbers))
            


def down(depth, number, numbers):
    """print("Here")
    print (depth)
    print (number)
    print (numbers)"""
    total = number
    if depth < len(numbers)-4:
        for i in range(depth+1, depth+4):
            print(numbers[depth+i][number])
            total *= int(numbers[depth+i][number])
            #total *= int(numbers[depth][i])

    return total

def right(index, number, numbers):
    print("right")

def diagonal(depth, index, number, numbers):
    print("diagonal")

product_grid()