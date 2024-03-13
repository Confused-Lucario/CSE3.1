'''
string_list = ["W", "or", "l", "d!"]
int_list = [5, 15, -67, 191, 88, -23]
float_list = [2.2, -101.9, 60.0]
boolean_list = [False, False, True, False, True]
mixed_list = ["Hello", 2, "the", string_list]
empty = []

while True in boolean_list:
    boolean_list.remove(True)
print(boolean_list)
'''
sandwich_type = ""
subtotal = 0.0
order = []

# Explaining Menu Options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
order.append(input("Sandwich Choice: "))

# Calculating Sandwich Price
if "chicken" in order:
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif "tofu" in order:
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
elif "beef" in order:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25

# Beverage Choice
bev_choice = input("Do you want a beverage? yes or no")
if bev_choice == "yes":
    order.append(input("What size beverage would you like? SmallBev, MediumBev, or LargeBev"))
    if "smallBev" in order:
        print("You chose small, so $1.00")
        subtotal += 1
    if "mediumBev" in order:
        print("You chose medium, so $1.75")
        subtotal += 1.75
    if "largeBev" in order:
        print("You chose large, so $2.25")
        subtotal += 2.25

# Fries
fry_choice = input("Do you want french fries? Yes or No")
if fry_choice == "yes":
    order.append(input("What size fries would you like? SmallFry, MediumFry, or LargeFry"))
    if "smallFry" in order:
        supersize = input("Do you want to supersize that for $2? Yes or no")
        if supersize == "yes":
            fry_size = "large"
            subtotal += 2
        else:
            print("You chose small fries for $1")
            subtotal += 1
    elif "mediumFry" in order:
        print("You chose medium for $1.50")
        subtotal += 1.50
    elif "largeFry" in order:
        print("You chose large fries for $2")
        subtotal += 2

# Kethcup
order.append(float(input("HJow many ketup packets would you like? $0.25 each")))
if order[3] >= 0:
    subtotal += order[3] * .25

if bev_choice == "yes" and fry_choice == "yes":
    subtotal -= 1

print(order)

print(subtotal)