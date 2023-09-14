# Formatted strings are useful where u dynamically generate some texts with your variables
# Lets say we have 2 variables first name and last name
first = 'Fakhra'
last = 'Rabbani'
# With these 2 variables, let say we want to generate some text like
# Fakhra [Rabbani] is a coder
# How do we print this on terminal?
message = first + ' [' + last + '] is a coder'
print(message) # Fakhra [Rabbani] is a coder

#This approach works but this is not ideal because as our text gets more complicated, it becomes harder to visualize the output
# This is where we use formatted strings, they make it easier for us to visualize the output
# Formatted string is the one that is prefixed with f then quotes -> f''.
# In between the quotes, we can use {} to add value of variable dynamically
msg = f'{first} [{last}] is a coder'
# This is what we call a formatted string
# With curly braces, we are defining place holders
# When our prgrm runs, these holes will be filled with value of variables
# With formatted string, we can easily visualize what the output looks like
print(msg)  # Fakhra [Rabbani] is a coder

# To define formatted strings, prefix your string with f and then use curly braces to dynamically insert values into your strings.
