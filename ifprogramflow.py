# __author__='dev'
# name = input("Please enter your name:
# age = int(input("How old are you, {0}?".format(name)))
# print(age)
#
# if (age >= 18):
#     print("You're old enough to vote! Good luck with that...")
# else:
#     print("Come back {0} years, {1}.".format(18 - age, name))
print ("Please guess a number between 1 and 10: ")
guess = int(input())

if (guess != 5):
    if (guess < 5):
        guess = int(input("Please guess higher: "))
    else:
        guess = int(input("Please guess lower: "))

    if (guess == 5):
        print("You got it!")
    else:
        print("Terminating upon failure...")

else:
    print("You got it on the first try!")
