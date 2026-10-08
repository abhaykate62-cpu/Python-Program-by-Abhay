# data types in python
a = 1 
b = 1 
# print(a)
print(a+b)
print(type(a))
# checking data type : integer

c = "1"
d = "1"
print(c+d)
print(type(c))
# checking data type : string

# basic data type in python :
#1. Numeric

a1 = 1      
#1a. integer

a2 = 1.5 
#1b. float
print(type(a2))

a3 = complex(3,5)
print(type(a3))
#1c. complex

#2. Sequence
b1 = "Madhav"
print(type(b1))
#2a. string

b2 = [1,4,7,26,108,'Madhav']
print(type(b2))
#2b. list

b3 = (1,4,7,26,108,'Madhav')
print(type(b3))
#2c. tuple

#3. dictionary
my_dict = {'name': 'Abhay','age': 18,'city':'Beed'}
print(type(my_dict))

#4. set
my_set = {1,2,3,4,5}
print(type(my_set))

#5. boolean
bool1 = True
bool2 = False
print(type(bool1))
print(type(bool2))



