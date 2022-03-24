# Checks that the user has inputed something in the correct formant, example here is with the date
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

Date_of_Joining = list()
count = 0
from datetime import datetime, date 

 # User enters date ~ Program outputs inputed value in the from of yy/mm/dd 
 # Program uses real time ~ If date entered is over or under 1 year, it outputs "That was a long time ago"
print("Enter a date ~ In the format of yyyy/mm/dd")
date_entry = input()
Year, Month, Day = map(int, date_entry.split("/"))
Date_of_Joining.append(datetime(Year, Month, Day,0,0))
print Date_of_Joining[count]
      
Time_Since_Joined = datetime.now()-Date_of_Joining[count]
if Time_Since_Joined.total_seconds()/(365.25*24*60*60) >= 1:
    print("That was a long time ago")
      
# ~ Explination of line 9:
# date_entry.split("/") - splits the string date_entry into a list at every "/", so 2021/03/21 gets turned into a list with elements ["2021", "03", "21"]
# map(int, date_entry.split("/")) - the map() function will loop through every element in the list provided as the second parameter and run the function provided in the first parameter (https://www.geeksforgeeks.org/python-map-function/). In this case the "int" is a builtin function which will convert every element into an integer from the string. So in the end ["2021", "03", "21"] will turn into [2021, 03, 21] (only the types of the values changed from string to int).
# Year, Month, Day = map(int, date_entry.split("/")) - finally, it will asign the first element of the array provided by the map() function into the Year variable, the second into the Month variable and the third into the Day variable. So you will end up with the Year holding the value 2021, Month with 3 and Day with 21.

# ~ Explination of line 13:
# datetime.now() - the current date and time in a single object
# datetime.now()-Date_of_Joining[count] - get the difference between the dates of now and the date that was gotten from the user before. The [count] part is there because Date_of_Joining is an array, meaning it has multiple elements and by adding [count] you specify what element in the array you want to use. The variable count should therefore represent the index of the current user.
# Time_Since_Joined = datetime.now()-Date_of_Joining[count] - store the difference between these two dates into a variable. In this case it does not have to be an array since this value does not need to be
# stored for every user but will be used just this once.

# ~ Explination of line 14 (where the numbers are multiplied):
# Time_Since_Joined.total_seconds() - this will give back the difference between the two dates calculated on line 7 in seconds
# Time_Since_Joined.total_seconds()/(365.25*24*60*60) - the difference in seconds divided by the amount of seconds in a year (365.25*24*60*60 = 31557600 aka how many seconds are in a year)
# if  Time_Since_Joined.total_seconds()/(365.25*24*60*60) >= 1: - if the difference in two dates is greater than 1 year, then do the thing inside this if statement 

# - What's a parameter? -
# In computer programming, a parameter or a formal argument is a special kind of variable used in a subroutine to refer to one of the pieces of data provided as input to the subroutine.
