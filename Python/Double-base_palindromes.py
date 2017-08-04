def find_palindrome():
    total = 0
    for i in range (1000000):
        if pal(i) and pal("{0:b}".format(i)):
            total += i
    print (total)

def pal(num):
    if str(num) == str(num)[::-1]:
        return True
    else: return False 

find_palindrome()