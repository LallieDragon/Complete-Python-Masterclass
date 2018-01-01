#First attempt
name = input("What is your name? ")
age = int(input("{}, how old beist ye? ".format(name)))

if (17 < age < 31):
    print("Welcome to the 18-30 holiday!")
elif (age < 18):
    print("Please come back in {} years.".format(18 - age))
else:
    print("Thank you for trying to make the holiday, but you've aged out.")
