import pandas as pd

grades = pd.Series([87,100,94])

#Pandas displays a Series in two-column format with the indices left aligned
#in the left column and the values right aligned in the right column.
#After listing the Series elements, pandas shows the data type (dtype) of
#the underlying array’s elements:

print(grades)


pd.Series(98.6, range(3))

print(pd.Series(98.6, range(3)))
#0    98.6
#1    98.6
#2    98.6
#dtype: float64
print()

#You can access a Series’s elements by via square brackets containing an index:

grades[0]
print(grades[0])

grades.count()
print(grades.count())

grades.mean()
print(grades.mean())

grades.min()
print(grades.min())

grades.max()
print(grades.max())

grades.std()
print(grades.std())
print()

# Calling Series method describe produces all these stats and more:

grades.describe()
print(grades.describe())
print()




# here is where the magic starts happening!
# You can specify custom indices with the index keyword argument:

grades = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])
print(grades)

# If you initialize a Series with a dictionary, its keys become the Series’ indices, and its values become
# the Series’ element values:

grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})
print(grades)
print()

# you can access individual elements via square brackets containing a custom index value:
grades['Eva']
print(grades['Eva'])
#100


#If the custom indices are strings that could represent valid Python identifiers, pandas automatically adds
#them to the Series as attributes that you can access via a dot (.), as in:

grades.Wally
print(grades.Wally)
#87

#Series also has built-in attributes. For example, the dtype attribute returns the underlying array’s element type:

grades.dtype
print(grades.dtype)
#dtype('int64')


grades.values
print(grades.values)
#array([ 87, 100, 94])
print()


#Series of Strings
hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])
print(hardware)

''' 0 Hammer
    1    Saw
    2 Wrench
    dtype: object'''


#calling string methods apply to each element
hardware.str.contains('a')
print(hardware.str.contains('a'))

''' 0     True
    1     True
    2    False
    dtype: bool '''



hardware.str.upper()
print(hardware.str.upper())

''' 0    HAMMER
    1       SAW
    2    WRENCH  '''
































