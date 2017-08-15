
def divisors(num):
    div = []
    for i in range(1, int(num/2)+1):
        if num%i == 0:
            div.append(i)
    
    return sum(div)

def amicable(num, div):
    if divisors(div) == num and div != num:
        return num
    else:
        return 0

total = set()

for i in range (2, 10000):
    total.add(amicable(i, divisors(i)))

print(sum(total))