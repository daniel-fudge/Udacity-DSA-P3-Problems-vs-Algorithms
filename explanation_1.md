# Problem 1 of the Data Structures Project
This solution finds the floored square root of the integer without using any Python libraries.    
This is accomplished with a modified binary search algorithm. Instead of looking for a specific number, we look for a 
number that once squared, matches the target squared value. If the value isn't found, as indicated with the left and 
right search bounds are adjacent to each other, we know the float square root value is between the bounds and the left 
bound is the floored integer value.    
Note in this implementation we don't create a list of integer to sort. Instead, we work directly with the moving bounds.
This reduces the space complexity to constant.  A binary search methodology was selected, since we know it to have the 
required time complexity of O(log n).

## Time Efficiency
As mentioned above the binary search methodology selected has a worse case time complexity of O(log n). This is a result 
of the search range dividing my half on every iteration.  In this case n is the size of the given squared value.
User test 3 also clearly illustrates the realized scaled time is greater than constant (growing) but vastly below n, 
which agrees with the O(log n) time complexity.

## Space Efficiency
As mentioned above, we do not create an array to search which would be O(n) in space complexity. However, this is a 
recursive implementation so the space efficiency is driven by the call stack size. Since in the worst case we would have 
to divide the range log(n) times, this creates a call stack log(n) deep.  This results in a space complexity of 
O(log n).   