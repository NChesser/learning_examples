with open('large_sum.txt') as f:
    result = [num.strip() for num in f]

total = 0
for i in result:
    total+= int(i)

print(str(total)[:10])