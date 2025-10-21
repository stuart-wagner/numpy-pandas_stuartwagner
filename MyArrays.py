import numpy as np



integers = np.array([[1,2,3],[4,5,6]])
print(integers)

floats = np.array([0.0,0.1,0.2,0.3,0.4])
print(floats)

for row in integers:
    for column in row:
        print(column, end=" ")      # prints every item in the array
    print()

for i in integers.flat:             # .flat makes an array a flat list
    print(i, end=" ")

print("\n")
zeros = np.zeros(5)
print(zeros)
print()

ones = np.ones((2,4), dtype = int)
print(ones)
print()

full = np.full((3,5), 13)           # .full makes an array containing only 1 number
print(full)
print()

myrange = np.arange(2, 10, 2)       #makes an array using a range() function (start,end,increment)
print(myrange)
print()

x = np.linspace(0.0,1.0,num=5)      # makes an array of awually seperated numbers/floats
print(x)
print()

y = np.arange(1,21).reshape(4,5)    # .reshape reshapes an array into the specified dimensions (must be able to fit)
print(y)
print()

z = np.arange(1, 100001).reshape(4,25000)
print(z)
print()

a = np.arange(1,100001).reshape(100,1000)   #printing will use ... to shorten printed arrays
print(a)
print()


# array opperators
numbers = np.arange(1,6)
print(numbers * 2)          # vectorized math
print(numbers ** 3)

numbers += 10               # can be done recursively
print(numbers)

numbers2 = np.linspace(1.1, 5.5, 5)
print(numbers2)
print(numbers * numbers2)   # multiplies items by items, must match length/dimension
print()


# comparing arrays
print(numbers)
print(numbers >= 13)        # operations/logic can be applied as well

print(numbers2)
print(numbers2 < numbers)





#LIST COMPREHENSION
#create a one-dimensional array from a list comprehension that produces even integers form 2 through 20

#integers = np.array([x for x in range(2,21,2)])





#You can produce evenly spaced floating-point ranges with NumPy’s linspace function. 
# The function’s first two arguments specify the starting and ending values in the range, 
# and the ending value is included in the array. The optional keyword argument num specifies 
# the number of evenly spaced values to produce—this argument’s default value is 50:








#Broadcasting

#Normally, the arithmetic operations require as operands two arrays of the same size and shape. 
# When one operand is a single value, called a scalar, NumPy performs the element-wise 
# calculations as if the scalar were an array of the same shape as the other operand, 
# but with the scalar value in all its elements. 


# multiplying integer arrays with floating pt arrays (result is floating pt)




#Comparing arrays

#You can compare arrays with individual values and with other arrays. 
# Comparisons are performed element-wise. Such comparisons produce arrays of 
# Boolean values in which each element’s True or False value indicates the comparison result:





























 

