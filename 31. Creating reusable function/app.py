# Reorganize the following code using a function
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😀",
    ":(": "😟"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)