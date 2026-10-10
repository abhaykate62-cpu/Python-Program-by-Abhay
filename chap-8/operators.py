# operators
                
# 1. Arithmetic operators
a = 5 
b = 3
print(a+b) # addition operator
print(a-b) # substraction operator
print(a*b) # multiplication operator
print(a%b) # modulus operator

# 2. Comparison operators - output value is boolean value(T/F)

a = 5
b = 3
print(a > b)  # greater than operator
print(a < b)  # less than operator
print(a == b) # equal operator
print(a != b) # not equal operator

# 3. Assignment Operators
a = 5  #('=' is assignment operator)

# 4. Logical operator

# Rule for AND operator
# 1. true + true = true
# 2. true + false = false
# 3. false + false = false

# Rule for OR operator
# 1. true + true = true
# 2. true + false = true
# 3. false + false = false

a = 10
b = 20
print(a>10 and b<10)  # and operator
print(a == 10 and b == 20)  # and operator
print(a == 10 or b == 10)  # or operator

# 'not' operator
print(not(a == 10 and b == 20))  # not operator
print(not(a == 10 or b == 20))   # not operator

# 5. Identity operator - is or is not
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # is operator
print(x is z)
print(x is not z)  # 'is not' operator

# 6. Membership operator - in , not in

my_list = ['apple' , 'orange' , 'watermelon']
print('apple' in my_list)
print('apple2'in my_list)
print('apple2'not in my_list)

7. Bitwise operators - AND '&' , '|' OR , XOR '^' ,NOT '~',etc
a = 5
b = 3
print(a & b)  # 5 = 101 , 3 = 011 , 5 & 3 = 001 = 1
print(a | b)  
print(a ^ b)  

