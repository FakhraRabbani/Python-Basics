# How to work with directories in Python?

# In python3 module index, we have a module called path lib
# path lib provides an object oriented file system pact
# That basically means it provides classes that we can use to create objects to work with directories and files.
# We can see on net how it works
# In basic usage, we can see how we import the path class from path lib module. -> from pathlib import Path
# P is capitalize which means its  a class. So it creates an instance of class.

# Lets import path class
from pathlib import Path
# Now we need to create a path object to reference a file or directory on our computer.
# There are basically two ways to do this
# We can use an absolute path or relative path which basically means a path starting from current directory.
# For eg, if u wanna reference ecommerce directory in our project, we can use the relative path. So we start from current directory and then go somewhere else.
# With absolute paths, we start from the roots of our hard disk.
# For eg if u are on windows, u might have an absolute path like this -> c:\Program Files\Microsoft. These are directories in c drive
# On windows we use a backslash to build a path.
# If u are on Mac or Linux, ur path will look a little bit different, instead of backslash we have forward slash -> /user/local/bin
# These were examples of absolute path

# We are going to work with relative path to work with this ecommerce directory that we have in our project.

# We create a path object Path()
# If we dont pass an argument here, this will reference the current directory
# Alternatively we can pass a string in which we can add a file or directory
path = Path("ecommerce")

# This path object has a few interesting methods.
# We can check to see if a path exists by calling the exist method which simply returns a boolean
# Exist Method
print(path.exists())  # True

# We can also create a new directory
# Lets change our path to emails
# When we run this prgrm, we obviuously dont have this directory
path1 = Path("emails")
print(path1.exists())  # False

# We can create this directory by calling the mk dir method
# mkdir Method (Make Directory)
# print(path1.mkdir())  # None
# It returns none which basically means it doesnt returns any value
# We can see in project panel that we now have a new directory for emails

# We can also delete this directory
# Instead of mkdir, we call rmdir(remove directory)
# path1.rmdir()

# Now we can see directory is gone.

# We can also find all the files and directories in a given path, that is very useful if you want to write a little prgrm to automate something
# For eg u can iterate over all the spreadsheets in a directory, open them and process them

# First we cahnge the path to current directory
pathh = Path()

# Then we call the glob method
# With glob method, we can search for files and directories in the current path.
# So first argument we need to pass a string that defines a search pattern.
# We can type an asteric that defines a search pattern. and that means everyting, all files and all directories.
# We can optionally add an extension so to get all the files you use *.*
# path.glob('*.*')
# Wth this pattern, we only get the files in the current directory. But not the directories.
# We can also search for all the py files or all the excel spreadsheets, anything
# Lets search for all the py files in the current directory
# print(path.glob('*.py'))
# When we run our prgrm, we get the generator object.
# We can iterate or loop through these generator objects.
# Instead of printing this generator object, lets iterate over it using a for...loop

for file in path.glob('*.py'):
    print(file)
# ecommerce\__init__.py
# We get all the py files in the current directory that is ecommerce

# We can use glob method to search for files using a pattern.
# We can also get all the files and directories in the current path, so we just use one asterik
for file in path.glob('*'):
    print(file)
# ecommerce\__init__.py



