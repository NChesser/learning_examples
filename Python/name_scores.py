import re
import string

with open('p022_names.txt') as f:
    names = f.read().split(",")

f.closed

number_score = 0
names.sort()

for i, name in enumerate(names):
    name = re.sub("\"", '', name)
    name_value = 0
    for c in name:
        name_value += string.ascii_lowercase.index(str(c).lower())+1
    
    number_score += name_value * (i+1)   
   
print (number_score)

