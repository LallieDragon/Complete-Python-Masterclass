import random


highest = int(input("Enter the highest number in your guessing range: "))
answer = random.randInt(1, highest)
attempts = 0

print("Please enter a number between 1 and {}".format(highest))
guess = 0
attempts += 1
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("{} was too low. Please guess again: ".format(guess))
        guess = int(input())
        attempts += 1

    elif guess > answer:
        print("{} was too high. Please guess again: ".format(guess))
        guess = int(input())
        attempts += 1


print("You guessed it correctly after {} tries.".format(attempt))
