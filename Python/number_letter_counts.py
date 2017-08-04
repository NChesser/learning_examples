
digits = ["one","two","three","four","five","six","seven","eight","nine"]
teens = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
number = ""
for i in range (1,1000):
    if i%100 == 0:
        number += digits[int(i/100)-1] + "hundred"
    elif i > 100:
        number += digits[int(i/100)-1] + "hundredand"
        i = i%100

    if i < 10:
        number += digits[i-1]
    elif i%10 == 0 and i < 100:
        number += tens[int(i/10)-1]
    elif i > 10 and i < 20:
        number += teens[i-11]
    elif i < 100 and i > 20:
        number += tens[int(i/10)-1] + digits[(i%10)-1]

number += "onethousand"

print (len(number))