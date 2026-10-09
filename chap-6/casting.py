# casting in python

a = 1
print(type(a))

b = "1"
print(type(b))

c = int(b)
print(type(c))

# print(type(a+b)) \\ it shows error because we can't add int and str
print(a+int(b))
print(a+c)

# all string type can't be casted into numerical type
# name = "Abhay"
# newname = int(name)\\ it shows error because we can't cvert str to int

# all numerical type can be cast into string type
mynum = 26
mynum2 = str(mynum)
print(type(mynum2))

f1 = 22.5
f2 = int(f1)
print(f2)
print(type(f2))

in1 = 26
print(type(float(in1)))
print(float(in1))

# implicit type casting
var1 = 10    #int type
var2 = 15.5  #float type
var3 = var1 + var2  
print(var3)
print(type(var3))

# explicit type casting
int_num = 101
str_num = str(int_num)
print(type(str_num))

a0 = bool(0)
print(a0)
print(type(a0))

a1 = bool(1)
print(a1)
print(type(a1))
