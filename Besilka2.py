import time
import random


name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")

print("")

time.sleep(1)

print("Start guessing...")

time.sleep(0.5)


guesses = ''
turns = 10

n = random.randint(0,9)
print(n)

zborovi = ["yummy","zephyr","zigzagging", "zombie", "zipper", "javascript", "hand", "hello", "green", "popcorn"]

word = zborovi[n]







while turns > 0:
    failed = 0


    for char in word:
        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You won")
        break

    print('')
    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
    print("You have", + turns, 'more guesses')
    if turns == 0:
        print("You Lose")