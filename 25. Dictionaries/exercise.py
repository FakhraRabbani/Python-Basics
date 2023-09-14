# Prgrm that asks for our phone number
# We type in digits like 1234 and then it will translate it into words One Two Three Four

# First we get users phone number
phone = input("Phone: ")

# Dictionary is a structure that allows us to map a key to a value
# "1" -> "One"

digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

# Noe we need to go through phone string
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# We set a default value ! in case we dont have number