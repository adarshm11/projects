print("Hello, let's start shopping.")
fruitCost = 0
applePrice = 3.99
bananaPrice = 2.99
orangePrice = 2.49
mangoPrice = 4.99

fruitArray = [["Apples", 3.99], ["Bananas", 2.99], ["Oranges", 2.49], ["Mangoes", 4.99]]
for fruit in fruitArray:
    print(fruit[0] + " cost $" + str(fruit[1]) + ". How many " + fruit[0].lower() + " would you like to buy?")
    amount = int(input())
    fruitCost = fruitCost + (amount * fruit[1])

print("Your items cost $" + str(round(fruitCost, 2)) + ".")
print("Thank you for shopping at Lucky's!")




