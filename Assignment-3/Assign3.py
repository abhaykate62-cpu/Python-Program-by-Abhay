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
    print(f"{year} is not year")