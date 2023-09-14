# We use dictionaries in situations where we want to store information that comes as key value pairs.
# Heres an example
# Think of a customer. A customer has a bunch of attributes like name, email, phone number, address and so on
# Now each of these attributes has a value.
# So what we have ehre is a bunch of key value pairs
# In this example, our keys are name, email and phone, and each key is associated with a value
# So this is where we use a dictionary
# With dictionary, we can store a bunch of key value pairs.

# With curly braces, we can define a dictionary
# customer = {}
# This is an empty dictionary which has no key value pairs
# We can add one or more key value pairs in between the braces
customer = {
    "name": "Fakhra Rabbani",
    "age": 18,
    "is_verified": True
}
# What matters here is that these keys should be uniquee. Duplication is not allowed. We cant add two keys od age
# Each key should be unique in dictionary

# We can access each item in dictionary using square brackets
# customer["name"] -> This will return value associated with  the name key
print(customer["name"])  # Fakhra Rabbani

# What if we pass a key that doesnt exist?
# print(customer["birthdate"])  # KeyError: 'birthdate'
# We gwt error because we dont have a key called birth date

# Also if we spell name with capital N, we get same error
# print(customer["Name"])  # KeyError: 'Name'

# We can get around using the get method
# GET METHOD
# So instead of using square brackets, we call the get method and specify the key
# If u use a key that doesnt exist here, it doesnt yell at us, it simply returns a none object
# None is an object that represents the absence of a value.
# Instead of getting key error, we get none
print(customer.get("name"))  # Fakhra Rabbani
print(customer.get("birthdate"))  # None

# We can also supply default value
# For eg if dictionary doesnt have the key, we can supply default value
print(customer.get("birthdate", "Nov 25 2004"))  # Nov 25 2004

# We can also update these values
customer["name"] = "Fakhra"
print(customer["name"])  # Fakhra

# We can also add a new key
customer["enrollmentdate"] = "Nov 24 2021"
print(customer["enrollmentdate"])  # Nov 24 2021

