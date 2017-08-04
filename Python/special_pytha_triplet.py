import math

print(math.sqrt(1000))

print (1000**2)
print(24**2 + 640**2 + 768**2)
print(24 + 640 + 768)

count = 1
"""for i in range (count, 1000):
    count +=1
    for j in range (count, 1000):
        for k in range (count, 1000):
            #print (str(i) + " " + str(j) + " " + str(k) + " " + str((i**2) + (j**2) + (k**2)))
            if ((i**2) + (j**2) + (k**2) == 1000**2):
                print (str(i) + " " + str(j) + " " + str(k))
                print((i**2) + (j**2) + (k**2))
                print(1000**2)
                break"""

for i in range(count, 100):
    for j in range(count, 100):
        if (i**2) + j**2 == 1000:
            print (str(i) + " " + str(j))
    