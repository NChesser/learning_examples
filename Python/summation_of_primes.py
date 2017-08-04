import math

def primes():
    count = 0

    for i in range (2, 2000000):
        
        prime = True

        for j in range (2, int(math.sqrt(i))+1):
            if i % j == 0:
                prime = False
                break
        
        if prime:
            print(i)
            count += i

    return count

print (primes())



        