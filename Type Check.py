# It ensures the user input is the correct data type using the try method.
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

def type_check(message):
   while True:
       try: # If the user does not type an integer, it will just ask the user to reinput the data
           user_input = int(input(message))
           return user_input      
       except ValueError:
           print("Please enter the correct class number")

Class_Number = type_check("Enter your class number please")
print("Thank you <3")
