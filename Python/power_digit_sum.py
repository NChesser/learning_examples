def power_digit_sum(n):
    
    num = [int(d) for d in str(n)]
    total = 0
    for d in num:
        total += d

    return total 

print(power_digit_sum(2**1000))

