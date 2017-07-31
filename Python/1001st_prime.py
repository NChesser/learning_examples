def primes():
    count = 0
    num = 1

    while count < 10001:
        num+=1
        prime = True

        for i in range (2, int(num/2)+1):
            if num % i == 0:
                prime = False
        
        if prime:
            print (num)
            count += 1

primes()



        