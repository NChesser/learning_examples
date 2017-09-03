import difflib

text1 = """
Nick
Hello
My
Name
ahasdlfj
nothing
adsfa
Is"""
text1_lines = text1.splitlines()

text2 = """
My
Hello
Is
Transform
Othering
sadfas
Nameasdf
Nick
Something"""
text2_lines = text2.splitlines()

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print ('\n'.join(diff))

if len(set(text1_lines)) > len(set(text2_lines)):
    print(set(text1_lines) - set(text2_lines))
else:
    print(set(text2_lines) - set(text1_lines))