chicken = 5.25
beef = 6.25
tofu = 5.75
total = 0.0

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
print("your sandwich price is $", total)