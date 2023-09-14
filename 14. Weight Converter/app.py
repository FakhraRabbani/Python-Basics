#Exercise
#Allow user to enter their weight in either kgs or pounds and then we will convert it into another unit

# weight = input("Weight: ")
# Weight is a string, we cant multiply or divide it with 0.45, so we will convert it into integer first
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

# We dont want the prgrm to be case-sensitive, so we will use upper method on unit string, whatever user enters in small or upper, it will be converted to upper and we will match it with capital one


if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} lbs")