# Write a prgrm to find the largest number in a list

numbers = [ 3, 6, 10, 4, 8]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)