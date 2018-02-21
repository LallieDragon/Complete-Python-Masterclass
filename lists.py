parrot_list = ["dumb", "flying", "in Europe"]

parrot_list.append("crazy")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
sortedNumbers = sorted(numbers)

print(sortedNumbers)

if sortedNumbers == sorted(numbers):
    print("The lists are equal.")
else:
    print("Lists are not equal")
