# input function in python

# a = input()
# print(int(a)+int(a))
# input function always reads input value as a string

name = input("Enter your name: ")
print(f"welcome {name} to python Tutorial series")


age = input("Enter your age: ")
print(f"Your age is {age}")
print(f"so next year you will be {int(age)+1}!")

x = input("Enter a number: ")
y = input("Enter second number: ")
print(f"The sum of {x} and {y} is {int(x) + int(y)}")

# H.W
# write a program to input student name and marks of 3 subjects
# print name and percentage of student

student_name = input("Enter student name: ")
marks1 = input("Enter marks of subject sub1: ")
marks2 = input("Enter marks of subject sub2: ")
marks3 = input("Enter marks of subject sub3: ")
percentage = (int(marks1) + int(marks2) + int(marks3)) / 3
print(f"Student Name: {student_name}")
print(f"Marks of subject 1: {marks1}")
print(f"Marks of subject 2: {marks2}")
print(f"Marks of subject 3: {marks3}")
print(f"Percentage: {percentage:.2f}%")


