shoppingList = ["milk", "eggs", "sugar", "flour", "spam"]

for item in shoppingList:
    #continue: If item is 'spam', loop will continue past it
    if item == "spam":
        print("I'm ignoring {}".format(item))
        continue
    print("Buy {}".format(item))

meal = ["egg", "bacon", "spam", "sausages"]

nasty = ''
for item in meal:
    #break: if item is spam, will end loop there.
    if item == 'spam':
        nasty = item
        break

if nasty:
    print("Cant eat anything with {} in it".format(nasty))
