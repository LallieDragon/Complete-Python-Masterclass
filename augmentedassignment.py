number = "9,223,372,036,854,775,807"
cleanNumber = ''

for char in number:
    if char in '0123456789':
        cleanNumber += char

newNumber = int(cleanNumber)
print(newNumber)

#Addition
x = 23
x += 1
print(x)
#Result 24

#Subtraction
x -= 4
print(x)
#Result 20

#Multiplication
x *= 5
print(x)
#Result 100

#Division
x /= 4
print(x)
#Result 25.0

#Exponential
x **= 2
print(x)
#Result 625.0

#Remainder/Modulo
x %= 60
#Result 25.0
