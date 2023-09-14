# We have a secret no which is set to 9
# Now the computer is asking me to make a guess.
# We only have 3 chances to make a guess.
# If i cant guess the number, the prgrm tells me i failed
# If i guess it, prgrm says u win

secret_number = 9

# What is condition here? Well we want to give our user maximum of 3 guesses
# So we can define a variable i, and give conditon until i is less than 3
# Lets use guess_count instead of i and use guess_limit instead of 3

guess_count = 0
guess_limit = 3

# break statement is used to terminate the loop. We need to jump out of loop if user wins
# In python, our while loops can also optionally have else part like if
# Our else block will execute if while loop executes without break
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry you failed!")



