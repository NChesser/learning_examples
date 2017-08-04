def find_largest_palindrome():
    largest = 0
    for i in range (900, 999):
        for j in range(900, 999):
            num = i * j
            if pal(num):
                largest = num
    print (largest)

def pal(num):
    if str(num) == str(num)[::-1]:
        return True
    else: return False 

find_largest_palindrome()