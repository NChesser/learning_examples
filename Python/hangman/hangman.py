import random
import string
import json
import difflib

with open('english-words.json.txt') as data:
    d = json.load(data)

made_guesses = []
hangman = ["""\
_________
""",
"""\
|
|
|
|
_________
""",
"""\
______
|
|
|
|
_________
""","""\
______
|    |
|
|
|
_________
""",
"""\
______
|    |
|    O
|
|
_________
""",
"""\
______
|    |
|    O
|    |
|
_________
""",
"""\
______
|    |
|    O
|   /|
|
_________
""",
"""\
______
|    |
|    O
|   /|-
|
_________
""",
"""\
______
|    |
|    O
|   /|-
|   /
_________
""",
"""\
______
|    |
|    O
|   /|-
|   / -
_________

*** YOU ARE DEAD ***
""",
]

def hang(data):
    word = random.choice(data)
    print(word)

    guesses = 0
    possible_guesses = list(string.ascii_lowercase)
    found = ["_"] * len(word)
    print (found)

    while guesses < len(hangman):      

        guess = random.choice(possible_guesses)
        possible_guesses.remove(guess)

        print ("Guessing " + guess)

        if(guess not in word):
            guesses += 1

        for i, l in enumerate(word):
            if l.lower() == guess:
                found[i] = guess
                print ("Correct ")
                print (found)

                if(make_guess(''.join(found), data) == word):                    
                    print ("Congratulations You Guessed Correctly")
                    return

        print (hangman[guesses-1])                
                

def make_guess(part, data):
    guesses = difflib.get_close_matches(part, data, n=100, cutoff=0.6)
    for guess in guesses:        
        if len(guess) == len(part):
            wrong = False 
            for i in range(0, len(part)):
                if part[i] != "_":
                    if part[i] != guess[i]:
                        wrong = True;
            if not wrong and guess not in made_guesses:
                print ("Making Guess " + guess)
                made_guesses.append(guess)
                return guess

hang(d)           


