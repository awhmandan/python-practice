import random

number = random.randint(1, 100)

guesses_taken = 0

while guesses_taken < 7:

	guess = int(input("I'm thinking of a number between 1 & 100... "))

	guesses_taken = guesses_taken + 1

	if guess == number:
		break
	elif guess < number:
		print("Too low guy!")
	elif guess > number:
		print("Too high my friend!")

if guess == number:
	print("Nice guessing skills dude, you got it in " + str(guesses_taken) + " guesses!")

if guess != number:
	print("Ahhhh, nope... The number was " + str(number) + " - next time!")
