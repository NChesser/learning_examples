import math
import itertools

def prime_factor(factors):
    for f in factors:
        for i in range (2, int(f/2)):
            if f%i == 0:
                break
        else:
            print(f)
    return factors

flatten_iter = itertools.chain.from_iterable
def factors(n):
    return set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0))    

prime_factor(factors(600851475143))