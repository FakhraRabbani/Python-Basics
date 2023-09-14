# In previous code, if we type start we get Car started again and again whenever we type start
# When user starts the car, it should print car started
# When user again starts the car, it should say car already started
# Same with the stop command

# In this prgrm, we need to know if the car is started or not.
# We need to store this one more piece of information in the memory
# So what is the kind of data we need to store here?
# A boolean -> Is the car started or not

command = ""
started = False


while True:
   command = input("> ").lower()
   if command == "start":
       if started:
           print("Car is already started")
       else:
           started = True
           print("Car Started...")
   elif command == "stop":
       if not started:
           print("Car is already stopped!")
       else:
           started = False
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