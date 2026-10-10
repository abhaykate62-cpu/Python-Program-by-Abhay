# Conditional Statement in python

# 1. if statement

a = 26
b = 108
if b > a:
    print("b is greater than a")
    

age = int(input("Enter your age"))
if age > 16:
    print("you are an adult")


# 2. if-else statement
age = int(input("Enter your age"))
if age > 16:
    print("Your are an adult")
else:
    print("Your are not an adult")


temp = 30

if temp < 25 :
     print("It's a cool day")
else:
    print("It's a hot day")  


# 3. if-elief-else statement 
#  multiple condition 

marks = int(input("Enter your marks-100:"))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade:B")
else:
    print("Grade: C")


# 4. Nested if-else statement
# if-else inside if-else statement
# multiple condition depend on each other


# Q: positive, negative & zero. positive - even/odd
number = int(input("Enter a number: "))

if number > 0:  #checking positive number
    if number % 2 == 0:
         print("This is a even number")
    else:
         print("This is a odd number")
else:
    if number == 0:
        print("This is zero")
    else:
        print("This is a negative number")



# 5. conditional expression (ternary operator)

age = 26
status = "Major" if age >= 18 else "Minor"
print(status)