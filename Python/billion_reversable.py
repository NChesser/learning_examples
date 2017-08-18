
def reverse(num):
    return int(str(num)[::-1])

def pal(num):
    for n in str(num):
        if int(n)%2 == 0:
            return False
    return True

def reversible(num):
    total = num + reverse(num)
    if pal(total) and num%10 != 0:
        return 2
    return 0    

total = 0
increment = 2
i = 0

while i < 10**9:
    if int(str(i)[0])%2 == 0 and i>10:
        increment = int(str("1"+"0"* ((len(str(i))-1))))
    else:
        increment = 2
    print(i)
    total += reversible(i)

    i += increment

print(total)