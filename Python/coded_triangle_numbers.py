import string

def trangular_number(n):
    return sum(range(n + 1))

triangles = [trangular_number(i) for i in range(100)]

def is_triangle(word):
    word = word[1:-1]
    total = 0
    for s in word:
        total += string.ascii_lowercase.index(s.lower())+1
    
    if total in triangles:
        return True
    
    return False   

with open("p042_words.txt", "r") as f:
    words = f.read().split(",")

print(len([w for w in words if is_triangle(w)]))