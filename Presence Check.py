# Checks that the user has actually inputed something
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

User_name = input('Please enter your name') # This makes the inputed thing by the user as their name
while User_name == "": # If the user enters nothing and leaves it blank, then an output message with error will be displayed
  User_name = input('Error, please enter your name') # The error message for leaving it blank
print('Hello ' + (User_name)) # If the user entered something, it will display "Hello" and their name ~ Which is what they inputed
