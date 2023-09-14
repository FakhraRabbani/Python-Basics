x = 10 + 3 * 2
# What do u think the result is?
# The ans is 16

# Operator Precedence -> Order of operations
# Multiplcation has higher precedence, so it gets executed first, 3 * 2 = 6 , then 6 is added to 10, so 16
print(x)  # 16

# This is the order
# 1. Parenthesis
# 2. Exponentiation 2 ** 3 => 8
# 3. Muliplication or division
# 4. Addition or Subtraction

y = 10 + 3 * 2 ** 2
# 2 ** 2 = 4, 3* 4 = 12, 10 + 12 = 22
print(y)  # 22

z = (10 + 3) * 2 ** 2
# 10 + 3 = 13, 2**2 =4, 13 * 4 = 52
print(z)  # 52

