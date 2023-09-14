# Use logical operators where we have multiple conditions

# Lets say we are building an application for processing loans. If an applicant has high income and good credit, then they are eligible for loan.
# So in this example, we have two conditions
# One is having high income and the other is having good credit
# So if both these conditions are true, then the applicant is eligible for loan.
# So this is where we use the logical and operator
# We use this operator to combine two conditions

has_high_income = False
# has_high_income = True
has_good_credit = True
# has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

# Logical or operator is used in situations where we want to do certain things if atleast one of the conditions is true

# Lets change the rule for prgrm
# If applicant has high income or good credit, they are eligible for loan
# So if either or both these conditions are true, then candidate is eligible

if has_high_income or has_good_credit:
    print("Eligible for loan")

# Logical AND: Both should be true
# Logical OR: Atleast one condition should be true
# Logical NOT: Inverses any boolean value we give it

# Lets make a new rule
# If applicant has good credit and doesnt have a crminal record, then they are eligible for loan

has_criminal_record = False
# has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
