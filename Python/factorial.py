def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


fact = factorial(100)

def sum_of_factorial(n):
    
    num = [int(d) for d in str(n)]
    total = 0
    for d in num:
        total += d

    return total 

print(sum_of_factorial(fact))

