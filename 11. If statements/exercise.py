# Imagine the price of a house is 1 million dollars
# Now if the buyer has good credit, they will need to put down 10 percent of price of property
# Otherwise they need to put down 20 percent
# Write a prgrm with these rules and display the down payment card for buyer with good credit

price = 1000000
# has_good_credit = True
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
#Formatted string
print(f"Down Payment: ${down_payment}")