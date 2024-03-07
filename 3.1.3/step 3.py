chicken = 5.25
beef = 6.25
tofu = 5.75
dsmall = 1
dmedium = 1.75
dlarge = 2.25
fsmall = 1
fmedium = 1.50
flarge = 2
total = 0.0
z = ""
s = ""
r = ""
l = ""

x = input(print("select a sandwich type, Chicken: $5.25, Beef: $6.25, Tofu: $5.75"))
if x == "chicken":
    print("you have seleted chicken")
    total = chicken + total
elif x == "beef":
    print("you have selected beef")
    total = beef + total
elif x == "tofu":
    print("you have selected tofu")
    total = tofu + total

y = input(print("would you like a beverage?, yes or no"))
if y == "yes":
    z = input(print("what size would you like?, Small: $1.00, Medium: $1.75, Large: $2.25"))
elif y == "no":
    print("you have selected no beverage")

if z == "small":
    print("you have selected small drink")
    total = dsmall + total
elif z == "medium":
    print("you have selected medium drink")
    total = dmedium + total
elif z == "large":
    print("you have selected large drink")
    total = dlarge + total

f = input(print("would you like fries?, yes or no"))
if f == "yes":
    s = input(print("what size would you like?, Small: $1.00, Medium: $1.50, Large: $2.00"))
elif f == "no":
    print("you have selected no fries")

if s == "small":
    l = input(print("would you like to mega size your fries?, yes or no"))
    if l == "no":
        print("you have selected small fries")
        total = fsmall + total
    elif l == "yes":
        print("you have selected mega fries")
        total = flarge + total
elif s == "medium":
    print("you have selected medium fries")
    total = fmedium + total
elif s == "large":
    print("you have selected large fries")
    total = flarge + total

r = input(print("how many ketchup packets would you like?"))
r = int(r)
total = total + abs(r) * .25

if y == "yes" and f == "yes":
    total = total - 1.00
if x == "chicken":
    print("you have seleted chicken")
elif x == "beef":
    print("you have selected beef")
elif x == "tofu":
    print("you have selected tofu")

if z == "small":
    print("you have selected small drink")
elif z == "medium":
    print("you have selected medium drink")
elif z == "large":
    print("you have selected large drink")

if l == "no":
    print("you have selected small fries")
elif l == "yes":
    print("you have selected mega fries")
elif s == "medium":
    print("you have selected medium fries")
elif s == "large":
    print("you have selected large fries")



print("your sandwich price is $", total)