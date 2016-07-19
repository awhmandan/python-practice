from time import sleep
import random

guess = input("Two dice, one roll - make your guess! ")
guess = int(guess)

sleep(2)

roll = random.randint(2, 12)
print(roll)

sleep(1)

if guess == roll:
	print("Lucky guess friend - good job!")
elif guess < roll or guess > roll:
	print("Snake eyes - better luck next time!")