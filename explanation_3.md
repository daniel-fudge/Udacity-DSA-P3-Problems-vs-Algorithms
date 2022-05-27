# Problem 3 of the Data Structures Project
To create two numbers from a given set of digits that sum to a maximum value, simply compile the two numbers with the 
highest digits at the front of the two new numbers. So this problem becomes a sorting problem with the desired time 
complexity of O(nlog n). To achieve the worst case time complexity, the merge sort algorithm was selected. On average
quick sort is O(nlog n), but worst case it is O(n^2).    
Slicing the array when passing the halves to the merge and mergesort sub-functions was also avoided to reduce both the 
space and time complexity. Instead of slicing the array, the left, mid and right indices were tracked to define the 
sub-arrays.  Slicing in Python has a time complexity of O(n) and would have resulting in many copies in the call stack.

### Assumptions
1. Digits are integers on the range [0, 9]

## Time Efficiency
The compilation of the two numbers has to pass through all the digits, so it has a time complexity of O(n). As mentioned 
previously, the worst case time complexity of the merge sort algorithm is O(nlog n).  Therefore, the total time 
complexity of this algorithm is O(n) + O(nlog n) = O(nlog n), where n = size of the input array.    
User test set 3, illustrates the O(nlog n) time complexity.

## Space Efficiency
As mentioned previously, the array was never sliced to make copies of the sub-arrays. Instead, the array was sorted 
inplace to maintain a constant space complexity. The only new array is a temporary output array in the merge function 
used to update the array values. This additional output array makes the space complexity O(n). The call stack is binary 
tree with a height of O(log n), which is traversed depth first.  Therefore, the call stack space complexity is O(log n) 
making the total space complexity = O(n) + O(log n) = O(n).