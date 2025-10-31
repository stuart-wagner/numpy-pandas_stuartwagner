import numpy as np
import random

# ROWS - each student
# COLS - each test

grades = np.array([[87, 96, 70], [100, 87, 90],[94, 77, 90],
                   [100, 81, 82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())
print()


'''
Many calculation methods can be performed on specific array dimensions,
known as the array’s axes. These methods receive an axis keyword argument
that specifies which dimension to use in the calculation, giving you a
quick way to perform calculations by row or column in a two-dimensional array.'''

grades_by_test = grades.mean(axis=0)    # "axis = 0" calculates averages by column
print(grades_by_test)

grades_by_student = grades.mean(axis=1) # "axis = 1" calculates averages by row
print(grades_by_student)
print()


'''NumPy offers dozens of standalone universal functions (or ufuncs) that perform various element-wise operations.'''


#Let’s create an array and calculate the square root of its values, using the sqrt universal function:
num07 = np.array([1,4,9,16,25,36])
num08 = np.sqrt(num07)
print(num08)
print()



# Let’s add two arrays with the same shape, using the add universal function:
num09 = np.array([10,20,30,40,50,60])
num10 = np.add(num07, num09)
print(num10)
print()




# Let’s use the multiply universal function to multiply every element of numbers2 by the scalar value 5:
num11 = np.multiply(num09,5)
print(num11)
print()



# Let’s reshape numbers9 into a 2-by-3 array, then multiply its values by a one-dimensional array of three elements:
num12 = num09.reshape(2,3)
num13 = np.array([2,4,6])

num14 = np.multiply(num12, num13) #applues the 1 dimensional array to each row
print(num14)
print()





# Indexing and Slicing

# To select an element in a two-dimensional array, specify a tuple containing the element’s row and column indices
# in square brackets (as in snippet [4]):

grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])





# You can select subsets of the columns by providing a tuple specifying the row(s) and column(s) to select.
# Each can be a specific index, a slice or a list. Let’s select only the elements in the first column:

student1 = grades[1]
print(student1)
print()


student0_test1 = grades[0][1]
print(student0_test1)
print()

'''
to select multiple _sequential_ rows, use ':'
'''
student0_1 = grades[0:2]    #upper limit (2) is not included
print(student0_1)
print()


# to select multiple _non sequential_ rows, use ','
students1and3 = grades[[1,3]]
print(students1and3)
print()

# to select students 1 and 3, but only test 2
students1and3_test2 = grades[[1,3],2]
print(students1and3_test2)
print()

# all students for test 0
all_students_test0 = grades[:,0]    # ':' without any numbers/arguments assumes all rows/entries
print(all_students_test0)
print()

all_students_test_1_2 = grades[:,1:3]
print(all_students_test_1_2)
print()

all_students_test0and2 = grades[:,[0,2]]
print(all_students_test0and2)
print()




''' EXERCISE
Use NumPy random-number generation to create an array of twelve random grades
in the range 60 through 100, then reshape the result into a 3-by-4 array.
Calculate the average of all the grades, the averages of the grades for each test
and the averages of the grades for each student.
'''
random_list = [random.randrange(60,101) for i in range(1,13)]
grades = np.array([random_list]).reshape(3,4)
print("Random Grades:\n", grades, "\n")
print("Average grade:            ", grades.mean())
print("Average grades by test:   ", grades.mean(axis=0))
print("Average grades by student:", grades.mean(axis=1))
print()




#Shallow copies (view)

#The array method view returns a new array object with a view of the original array
numbers = np.arange(1,6)
numbers_view = numbers.view()

print(numbers)
print(numbers_view)

numbers[1] *= 10
print(numbers_view) # the 'view' copy updated with the numbers original

numbers_view[1] /= 10
print(numbers)      # changes to the 'view' copy also affect the original
print()



#Slice Views

#Slices also create views. Let’s make numbers2 a slice that views only the first three elements of numbers:
numbers_slice_view = numbers[0:3]
print(numbers_slice_view)

numbers[1] *= 20
print(numbers_slice_view)   # 'view' rules apply to slices/'sliced views'
print()




#Deep copies
#The array method copy returns a new array object with a deep copy of the original array
numbers_copy = numbers.copy()

print(numbers_copy)

numbers[1] *= 10        # copy versions do not affect the original
print(numbers)
print(numbers_copy)
print()





'''The array methods reshape and resize both enable you to change an array’s dimensions. Method reshape returns a
view (shallow copy) of the original array with the new dimensions. It does not modify the original array:'''


grades = np.array([[87, 96, 70], [100, 87, 90]])
grades_reshaped = grades.reshape(1,6)   # 'reshape' makes a 'view' of the original
print(grades_reshaped)
print(grades)

grades.resize(1,6)  # 'resize' alters the original
print(grades)

grades = np.array([[87, 96, 70], [100, 87, 90]])
flattened = grades.flatten()
raveled = grades.ravel()
print(grades)
print(flattened) #deep copy
print(raveled)  #shallow copy

print(grades.T) #transpose function
print()







#You can quickly transpose an array’s rows and columns—that is “flip” the array, so the rows become the columns and
#the columns become the rows. The T attribute returns a transposed view (shallow copy) of the array. 






#You can combine arrays by adding more columns or more rows—known as horizontal stacking and vertical stacking.

#HSTACK





#VSTACK

#let’s assume that grades2 represents two more students’ grades on three exams.



























