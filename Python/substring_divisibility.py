import itertools

def substring_divisibility(num):
    if not int(num[1:4])%2 == 0:
        return False
    elif not int(num[2:5])%3 ==0:
        return False
    elif not int(num[3:6])%5 ==0:
        return False
    elif not int(num[4:7])%7 ==0:
        return False
    elif not int(num[5:8])%11 ==0:
        return False
    elif not int(num[6:9])%13 ==0:
        return False
    elif not int(num[7:10])%17 ==0:
        return False
    
    return True

pandigital = "1234567890"

perm = list(itertools.permutations(pandigital, len(pandigital)))

print(sum([int(''.join(ssd)) for ssd in perm if substring_divisibility(''.join(ssd))]))

