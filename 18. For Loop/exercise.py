# Write a prgrm to calculate the total cost of all the items in a shopping cart
# Lets say we have a list of prices like 10, 20, 30
# I want you to use a for...loop to calculate the total cost of all items in our imaginary shopping cart
# Calculate that and print it on terminal

prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f"Total: {total}")