# With dictionaries , we can do something really cool
# We can type a message like good morning followed by a smiley face and when we press enter we get smiley face

# We have dictionary that maps these characters into smiley faces.

# We start by calling input function
message = input(">")

# No we need to split the string by space
# If user type Good morning :), it will get broke down to three words good, morning and smiley face

words = message.split(" ")
# This method basically goes through this string and anywhere it finds this " " character in this case a space, it uses it a a boundary to separate string into multiple words
# Ans then it will return a list.
print(words) # ['Good', 'Morning', ':)']

# Now we need to define a dictionary to map a special chracter like these two :) into a smiley face

# How to add emoji in string?
# window key plus dot

emojis = {
    ":)": "😃",
    ":(": "😔"
}

output = ""
# Now we have list of words
# Now we need to look through this let, get each word and map it to an emoji

for word in words:
    output += emojis.get(word, word) + " "

print(output)

# If we have the word map, we get that. If we dont have we just get the word value as it is .. default