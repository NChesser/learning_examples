import itertools

with open('series1.txt') as f:
    numbers = f.read().splitlines()

numbers = list(itertools.chain.from_iterable(list(numbers)))
largest = 0


for i, num in enumerate(numbers):
    total = int(num)
    if i < len(numbers)-12:
        for v in range (i+1, i+13):
            total *= int(numbers[v])
        if total > largest:
            largest = total
        
print (largest)
