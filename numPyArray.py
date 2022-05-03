# -*- coding: utf-8 -*-
"""
This is the "longhand" version of using NumPy Array functionality
to calculate the square of every element in an array.

"""
# Declare an array ("little a") as a List of List objects
anArray = [ [ 0.0, 0.1, 0.2, 0.3 ], 
            [ 1.0, 1.1, 1.2, 1.3 ],
            [ 2.0, 2.1, 2.2, 2.3 ]  ] 

print( "Original array values " )
print( anArray )

"""
    Use a two-level (for two dimensions) nested loop to calculate the
    squares and to store the results into a new array ("little a")
    
    (This is something that NumPy can do for us - we'll look at that later.)        
"""
squared = []                        # Declare the List to hold the new array
for row in anArray:                 # Process each ROW of the array
    rowList = []                    # Declare a List to hold results / row
    for element in row:             # Process each element / column in ROW
        square = element**2
        rowList.append( square )    # Insert results into ROW level List
    # end element within row 
    squared.append( rowList )       # Insert ROW level List into array
# end row within array

print( "New array with squared values " )
print( squared )


#------------------------------------------------------------------------------

"""
Our Array object will hold numbers the same numbers:
    
           Col 0     Col 1      Col 2     Col 3
           ------    ------     -----    ------
    Row 0     0.0       0.1       0.2       0.3
    Row 1     1.0       1.1       1.2       1.3
    Row 2     2.0       2.1       2.2       2.3
    
"""
import numpy as np

#=========================   Initial Instantiation & Load of an Array

anArray = np.array( [ [ 0.0, 0.1, 0.2, 0.3 ], 
                      [ 1.0, 1.1, 1.2, 1.3 ],
                      [ 2.0, 2.1, 2.2, 2.3 ]  ] )

print( "Our initial Array object contents:" )
print( anArray )
print( "The 'shape' of our Array is: ", 
        anArray.shape, "\n" )

"""
    Use the built-in NumPy functionality to produce a NEW ARRAY containing
    the squared values of the ORIGINAL array.       
"""
# If we need to KEEP the RESULTS, we need to build a new Array based on them
squared = np.array( np.square( anArray ) )
print( "\n\nA new Array, results of squaring anArray: " )
print( squared )
print( "The 'shape' of our Array is: ", 
        squared.shape, "\n" )


