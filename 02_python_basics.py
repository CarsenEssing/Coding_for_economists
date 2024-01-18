#Basic Math in Python

#add numbers
print(2+4)

#Divide
print(10/5)

#careful division returns a float
print(type(10/5))

#exponents
print(2**3)

# assigning variables
x = 5
y = x ** 2
print(y)

#string
a = 'hello' #also a = "hello "

#arithmatic operations on strings
#multiplication
print(a*5)

#concentation
b = "whats up"
print(a + " " + b)

#subtraction
#print(a-b)-- DOES NOT WORK

#indexing and slicing
#first element
print(a[0])

#last element
print(a[-1])

#slicing
print(a[0:5])

# number of characters in an object
print(len(a))

#logical statements
print(2==2) # TRUE = 1
print(2==3) # FALSE = 0

print(true + true) # 1 + 1 = 2

# check equilivence of 2 variables
print(a == b and 3 == 3) #true
print(2 == 2 and 3 ==4) #false
print(2 == 2 or 3 ==4) #true