# Assignment 2: Python Programming


# Q.no.1
# Write a Python program to input student name and marks of 3 subjects, then calculate and print the name and percentage of the student.
# write name & percentage in output


student_name = input("Enter student name: ")
hindi_marks = input("Enter marks of subject Hindi: ")
english_marks = input("Enter marks of subject English: ")
math_marks = input("Enter marks of subject Math: ")



# Calculate percentage
 percentage = (int(hindi_marks) + int(english_marks) + int(math_marks) ) * 100 / 300



# print results
print(f"the result of {student_name} is {int(percentage)}%. Well done!!")




# Q.no.2
# write a program that collect multiple types of data to store in a dictionary
# print output


# Initializing a dictionary
user_data = {}


# input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student (Yes/No)")


# print the input from user
print(user_data)