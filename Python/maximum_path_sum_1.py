import random

lines = [line.rstrip('\n') for line in open('triangle1.txt')]

pyramid = []
for line in lines:
    pyramid_layer = []
    values = line.split()
    pyramid_layer = [v for v in values]
    pyramid.append(pyramid_layer)

largest = 0
for line in pyramid:
    biggest = 0
    for v in line:
        if int(v) > biggest:
            biggest = int(v)
    
    largest += biggest

print(largest)

def get_max(start=0, index=0, max_total=0):
    if start == 0:
        max_total += int(pyramid[0][0])
        get_max(start+1, index, max_total)
    elif start < len(pyramid):
        left = pyramid[start][index]
        right = pyramid[start][index+1]

        rand = random.randrange(2)        
        #if rand == 1:
        if int(left) > int(right):
            max_total += int(left)
            get_max(start+1, index, max_total)
        else:
            max_total += int(right)
            get_max(start+1, index+1, max_total)
    else:
        print(max_total)      

get_max()