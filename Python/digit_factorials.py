import math

def digit_factorial(num):
    digits = [math.factorial(int(n)) for n in str(num)]      
    return sum(digits) == num

print(sum([i for i in range(3, 10**6) if digit_factorial(i)]))

