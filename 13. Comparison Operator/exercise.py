# If name is less than 3 characters long -> name must be atleast 3 characters
# otherwise if its more than 50 characters long -> name can be a maximum of 50 characters
# otherwise -> name looks good!

name = input("Enter your name: ")
# name = 'F'

if len(name) < 3:
    print("Name must be atleast 3 characters long")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")
