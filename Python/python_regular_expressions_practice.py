import re

def is_allowed_character(string):
    return not re.match(r'[^a-zA-Z0-9.]', string)

print(is_allowed_character("asdfjaslf"))
print(is_allowed_character("(**(*(&78^%"))

def followed_by_zero_or_more_b(string):
    return not not re.search(r'ab*', string)

print(followed_by_zero_or_more_b("d"))
print(followed_by_zero_or_more_b("abbc"))
print(followed_by_zero_or_more_b("Nlabsdfdab"))

def followed_by_one_or_more_b(string):
    return not not re.search(r'ab+', string)

print(followed_by_one_or_more_b("ab"))
print(followed_by_one_or_more_b("abb"))
print(followed_by_one_or_more_b("asbdaf"))

def followed_by_one_or_zero_b(string):
    return not not re.search(r'ab?', string)

print(followed_by_one_or_zero_b("ab"))
print(followed_by_one_or_zero_b("abb"))
print(followed_by_one_or_zero_b("sbdf"))

def followed_by_three_b(string):
    return not not re.search(r'ab{3}', string)

print(followed_by_three_b("ab"))
print(followed_by_three_b("abbb"))

def followed_by_two_to_three_b(string):
    return not not re.search(r'ab{2,3}', string)

print(followed_by_two_to_three_b("ab"))
print(followed_by_two_to_three_b("abb"))
print(followed_by_two_to_three_b("abbbc"))

def upper_followed_by_lower(string):
    return not not re.search(r'(^[A-Z]?)+[a-z]', string)

print(upper_followed_by_lower("Abc"))
print(upper_followed_by_lower("ABc"))
print(upper_followed_by_lower("aBc"))

def a_followed_by_anything_ending_in_b(string):
    return not not re.search(r'(^a?)+.*b$', string)

print(a_followed_by_anything_ending_in_b("adsdfb"))
print(a_followed_by_anything_ending_in_b("adsdfd"))
print(a_followed_by_anything_ending_in_b("ab"))

def match_word_at_beginning(string):
    return not not re.search(r'^\w+', string)

print(match_word_at_beginning("Something Here"))
print(match_word_at_beginning(" Something Here"))

def match_word_at_end(string):
    return not not re.search(r'\w+\S$', string)

print(match_word_at_end("Something Here"))
print(match_word_at_end(" Something Here "))

def match_word_containing_z(string):
    return not not re.search(r'\w*z.\w*', string)

print(match_word_containing_z("Something Here"))
print(match_word_containing_z("Sometzhing Here "))

def match_word_containing_z_not_start_or_end(string):
    return not not re.search(r'\Bz\B', string)

print(match_word_containing_z_not_start_or_end("Zomething Here"))
print(match_word_containing_z_not_start_or_end("Sometzhing Here "))

def match_lower_upper_number_underscores(string):
    return not not re.search(r'^[a-zA-Z0-9_]*$', string)

print(match_lower_upper_number_underscores("Zomething Here"))
print(match_lower_upper_number_underscores("Sometzhing_Here_45"))

def start_with_number(string):
    return not not re.search(r'^[0-9]', string)

print(start_with_number("3asfas"))
print(start_with_number("323asfas"))
print(start_with_number("asfas"))

def remove_leading_zeros(string):
    return re.sub(r'\.[0]*', ".", string)

print(remove_leading_zeros("23.0343"))
print(remove_leading_zeros("10.007.02342"))

def check_number_at_end_of_string(string):
    return not not re.search(r'.*[0-9]$', string)

print(check_number_at_end_of_string("23.0343asf"))
print(check_number_at_end_of_string("10.007.02342"))

def find_numbers_between_one_and_three():
    return re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")

results = find_numbers_between_one_and_three()

for r in results:
    print(r.group(0))