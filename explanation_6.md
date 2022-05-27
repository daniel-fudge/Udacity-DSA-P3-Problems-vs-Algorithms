# Problem 6 of the Data Structures Project
This problem returns a tuple(min, max) out of list of unsorted integers in O(n) time without built-in functions. This is
accomplished by simply initializing a min and max value variable to the first value in the array and then traversing the
array once. For each element, the element value is compared to the saved min and max values and the values are updated
if a new extreme value is detected.

## Time Efficiency
As this is a single traversal, the time efficiency is O(n).    
User test set 3 confirms the O(n) time complexity.

## Space Efficiency
Since we simply save the min and max values to integer variables, the space efficiency is O(1).
