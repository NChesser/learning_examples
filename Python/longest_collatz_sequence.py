

def longest_collatz():
    longest = 0
    
    for i in range (1000000, 10, -1):
        collatz = check_collatz(i)
        if  longest < collatz:
            print(i)
            longest = collatz
            

def check_collatz(num):
    count = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num +=1
        count += 1
    
    return count+1

longest_collatz()

#print(check_collatz(13))