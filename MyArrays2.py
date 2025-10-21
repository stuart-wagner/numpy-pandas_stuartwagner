import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90],[94, 77, 90],
                   [100, 81, 82]])




'''
Many calculation methods can be performed on specific array dimensions,
known as the array’s axes. These methods receive an axis keyword argument
that specifies which dimension to use in the calculation, giving you a
quick way to perform calculations by row or column in a two-dimensional array.'''






'''NumPy offers dozens of standalone universal functions (or ufuncs) that perform various element-wise operations.'''


#Let’s create an array and calculate the square root of its values, using the sqrt universal function:




# Let’s add two arrays with the same shape, using the add universal function:





# Let’s use the multiply universal function to multiply every element of numbers2 by the scalar value 5:




# Let’s reshape numbers2 into a 2-by-3 array, then multiply its values by a one-dimensional array of three elements:






# Indexing and Slicing

# To select an element in a two-dimensional array, specify a tuple containing the element’s row and column indices
# in square brackets (as in snippet [4]):

grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])





# You can select subsets of the columns by providing a tuple specifying the row(s) and column(s) to select.
# Each can be a specific index, a slice or a list. Let’s select only the elements in the first column:










''' EXERCISE
Use NumPy random-number generation to create an array of twelve random grades
in the range 60 through 100, then reshape the result into a 3-by-4 array.
Calculate the average of all the grades, the averages of the grades for each test
and the averages of the grades for each student.
'''





#Shallow copies (view)

#The array method view returns a new array object with a view of the original array







#Slice Views

#Slices also create views. Let’s make numbers2 a slice that views only the first three elements of numbers:









#Deep copies
#The array method copy returns a new array object with a deep copy of the original array












'''The array methods reshape and resize both enable you to change an array’s dimensions. Method reshape returns a
view (shallow copy) of the original array with the new dimensions. It does not modify the original array:'''


grades = np.array([[87, 96, 70], [100, 87, 90]])













#You can quickly transpose an array’s rows and columns—that is “flip” the array, so the rows become the columns and
#the columns become the rows. The T attribute returns a transposed view (shallow copy) of the array. 






#You can combine arrays by adding more columns or more rows—known as horizontal stacking and vertical stacking.

#HSTACK





#VSTACK

#let’s assume that grades2 represents two more students’ grades on three exams.



























