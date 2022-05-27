# Problem 2 of the Data Structures Project
This problem is a modified search problem. The given array is already sorted but rotated so a standard binary search 
would not work. We could create a new sorted version of the given array but the slicing of the array would make the 
runtime complexity O(n). To maintain a time complexity of O(log n), we need to modify the binary search algorithm to 
adjust the indices each iteration to account for the rotation.  Therefore, this solution decomposes into two components 
each with a time complexity of O(log n).   
The first is a `find_pivot` function which is a modified binary search that finds the pivot. The pivot is defined as the 
largest value in the array, which exist before the first element of the array that is smaller than the first element of
the array; i.e. first i where array[i+1] < array[0].  
With this pivot value, the binary search is modified internally where index i = (i_sorted + pivot + 1) % n_elements. 
With this modification, it is a standard binary search with a time complexity of O(log n) as required.

### Assumptions
1. No duplicates in the array
2. The array elements are all integers

## Time Efficiency
As discussed above the two sub-functions have a time complexity of O(log n). Therefore, the total time complexity is 
O(log n) + O(log n) = O(log n), where n = the number of elements in the given array.  
User tests 4, 5 & 6 verify the O(log n) time complexity of the find_pivot, binary_search and overall 
rotated_array_search functions. 

## Space Efficiency
Clearly the input array is size n but since we are not making a copy of this array but searching inplace, the additional 
space complexity is constant. Unfortunately, both of the sub-functions are recursive so the space efficiency is driven 
by the call stack. Since the function are called in series, the space complexity with be the maximum of both functions.
Both functions are modified recursive binary searches so the call stack will have a space complexity of O(log n).   
Therefore, the total space complexity beyond the input array of size n, is O(log n).