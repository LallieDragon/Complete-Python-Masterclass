number = "1,934,223,982,746,807"
cleanNumber = ''

#Char will iterate through each character comparing it to the in "0123456789"
for char in number:
    if char in '0123456789':
        cleanNumber = cleanNumber + char

newNumber = int(cleanNumber)
print(cleanNumber)

#State will take each string in the array and append it in the print statement
for state in ["not pinin", "no more", "a stiff", "bereft of lift"]:
    print("This is parrot is " + state)

#i in range(beginning number, ending number, number to increment i with)
for i in range(0, 100, 5):
    print("i is {}".format(i))

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2},".format(i, j, i*j), end='\t')
    print('')
