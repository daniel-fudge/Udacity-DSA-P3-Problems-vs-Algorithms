# Problem 4 of the Data Structures Project
This solution sorts an input array consisting on only 0, 1, and 2. This is accomplished in a single traversal by sorting 
in place and leveraging the fact that there are only 3 possible values. Because there are only three values we don't 
really have to sort but place 0's at the start, 2's at the end and leave the 1's in the middle. This can all be done in 
a single while loop that tracks the next left and right position to place the ith element. Since the left, right or "i" 
index is incremented every loop, and we quit when i > right, we only traverse the array once.

### Assumptions
1. Array elements only sampled from [0, 2].

## Time Efficiency
As this is a single traversal algorithm, the time complexity is O(n).    
User test set 3 illustrates the O(n) time complexity.

## Space Efficiency
As this is an in-place sorting algorithm, the space complexity is O(1). 
