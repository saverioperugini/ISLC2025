#Python Program to Check Leap Year
#In this program, you will learn to check whether a year is leap year or not. We will use nested if...else to solve this problem.

#To understand this example, you should have the knowledge of the following Python programming topics:

#Python Operators
#Python if...else Statement
#A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,

#2017 is not a leap year
#1900 is a not leap year
#2012 is a leap year
#2000 is a leap year

# Python program to check if year is a leap year or not

def leapyear(year):

   leap = False

   # divided by 100 means century year (ending with 00)
   # century year divided by 400 is leap year
   if (year % 400 == 0) and (year % 100 == 0):
      leap = True
      #print("{0} is a leap year".format(year))

   # not divided by 100 means not a century year
   # year divided by 4 is a leap year
   elif (year % 4 ==0) and (year % 100 != 0):
      leap = True
      #print("{0} is a leap year".format(year))

   # if not divided by both 400 (century year) and 4 (not century year)
   # year is not leap year
   else:
      leap = False
      #print("{0} is not a leap year".format(year))

   return leap

# To get year (integer input) from the user

year=int(input("\nEnter a year: "))

leap = leapyear(year)

if leap:
   print(year, "is a leap year.\n")
else:
   print(year, "is not a leap year.\n")
