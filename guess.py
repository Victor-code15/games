""" Just a guess the number game that was made for me to learn.
How to execute: 'python3 guess.py '
"""
import random

NUMVICTOR = random.randrange(20)
acertou = False
while not acertou:
    guess = input('make a guess between 1 and 20: ')
    guess = int(guess)
    if guess == NUMVICTOR:
       print("Congrats you won!!!!")
       acertou = True
    elif guess > NUMVICTOR:
        print("Sorry, try again...")
        print('Hint:try a lower number next time')
    else:
        print("Sorry, try again...")
        print('Hint:try a higher number next time')