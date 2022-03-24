# Checks for a set length when user inputs data - Used name as an example here
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

print("State your name")
name = str(input())

while len(name) < 4:
     print("State a valid name")
     name = input()

while len(name) > 3:
 print("You can now write a comment")
 
 while len(name) > 3:
     input()
     print("Anything else you want to comment, " + name + "?")

      
