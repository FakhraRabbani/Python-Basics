# This game is simulation to car game
# Focus -> Building engine for this game
# When we run the prgrm, we get this symbol >, our prgrm is waiting for us to enter a command
# If u type help, we get list of commands that our prgrm or game currently supports.
# We can type start command to start our car
# We cana type stop command to stop our car
# We can type quit to terminate the game
# Any other commands we type, our prgrm is going to tell us hey i dont understand that...

# We will use while loop
# What is the condition? We want to continue this loop until user types quits
# So we will use a variable to store what command user types
# Loop continues until the command does not equal to quit

# Before loop, we set command variable to empty string
# An empty string is a string that has no characters in it.

command = ''

# while command.lower() != 'quit':
#    command = input("> ")
#    if command.lower() == "start":
#        print("Car Started...")
#    elif command.lower() == "stop":
#        print("Car Stopped.")

# We have repeated this term lower again and again. In programming, this is bad
# We have a term called dry in programming short for dont repeat yourself
# How we can solve this problem?
# Instead of calling lower method in each condition, we can call it right there when we get input from the user
# Input function returns a string, we can immediately call lower method on the string and with this command will always be in lower case

# If u look at code, we are kind of repeating statement of quit in elif and consition
# We can simplify our condition like this
# while True
# With this our block of code is going to get executed repeatedly, until we get explicitly break out of it


# while command != 'quit':
while True:
   command = input("> ").lower()
   if command == "start":
        print("Car Started...")
   elif command == "stop":
        print("Car Stopped.")
   elif command == "help":
       print(""" 
start - to start the car
stop - to stop the car
quit - to quit
       """)
   elif command == "quit":
       break
   else:
       print("Sorry, i dont understand that ...")

