# Assignment - 3

# Q.no.1 Leap year: write a simple program to
# Determine if a given year is a leap year
# using user input

# leap year condition:
# 4 divisible & 100 not divisible
# 400 divisible


# user input

year = int(input("Enter a year (e.g 2026):"))

# checking leap year
if (year %4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")

else:
    print(f"{year} is not leap year")



# Q.No.2 Login Authentication using conditional statement.
# Assume you have a predifined username and password.
# write a program that promts the user to enter a username and password.
# Both username and password are correct.
# username is correct but password is incorrect.
# username is incorrect.

# predefined username and password

predefined_username = "Abhay"
predefined_password = 'pass101'

# prompts the user to enter a username and password

Username = input("Enter your Username: ")
Password = input("Enter your Password: ")

# username and password match

if Username == predefined_username:
    if Password == predefined_password:
        print("Welcome! Login was successful...")
    else:
        print("Incorrect password")
else:
    print("Invalid Username")




# Q.No.3: Admission Eligibility :A university has the following 
# eligibility criteria for admission :
# Marks in mathematics >= 65
# Marks in physics >= 55
# Marks in chemistry >= 50
# total marks in all three subjects >= 180 OR 
# total marks in mathematics and physics >= 140
# write a program that takes marks in three subjects as input and 

# user input
print("Enter PCM marks out of 100")
physics_marks = int(input("Enter physics marks: "))
Chemistry_marks = int(input("Enter Chemistry marks: "))
Math_marks = int(input("Enter Math marks: "))

# Eligibility checks
if (Math_marks >= 65 and 
   physics_marks >= 55 and
   Math_marks >= 50 and
   (Math_marks + physics_marks + Chemistry_marks) >= 180 ) or \
   (Math_marks + physics_marks) >= 140 :
   print("you're eligible!")
else:
    print("you're Not eligible!")

