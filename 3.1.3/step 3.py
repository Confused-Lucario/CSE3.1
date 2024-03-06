chicken = 5.25
beef = 6.25
tofu = 5.75
small = 1
medium = 1.75
large = 2.25
total = 0.0
z = ""
x = input(print("select a sandwich type, Chicken: $5.25, Beef: $6.25, Tofu: $5.75"))
if x == "chicken":
    print("you have seleted chicken")
    total = chicken + total
elif x == "beef":
    print("you have selected chicken")
    total = beef + total
elif x == "tofu":
    print("you have selected tofu")
    total = tofu + total

y = input(print("would you like a beverage, yes or no"))
if y == "yes":
    z = input(print("what size would you like? Small: $1.00, Medium: $1.75, Large: $2.25"))
elif y == "no":
    print("you have selected no beverage")

if z == "small":
    print("you have selected small")
    total = small + total
elif z == "medium":
    print("you have selected medium")
    total = medium + total
elif z == "large":
    print("you have selected large")
    total = large + total
elif z != small or z != medium or z != large:
    print("selection is not a option")


print("your sandwich price is $", total)