# Problem 5 of the Data Structures Project
This problem follows a set Workbook from Udacity that was completed and saved [here](Trie.ipynb) as directed in the 
Udacity problem 5 description.   
This solution implements a Trie to represent a listing of words. The advantage of the Trie over a standard set is 
common prefixes are shared, making the time and space complexity O(n), where n is the unique character position. For 
instance, "i", "it", "item" and "items" together only have n = 5 nodes in the Trie, each with a single character. If 
stored as a set, it would have 4 elements, with a total of 12 characters.    
Note that "cook" has only 3 unique characters but n = 4 unique character positions.

## Time Efficiency
Since the find and insert methods of the trie completely traverse the given full path, their time complexity is O(n).    
User test set 4 confirms the insert and find time complexity with words with 10^5, 10^6 and 10^7 characters.

## Space Efficiency
Since find and insert method of the trie do not build any data structures or use recursive functions (no call stack), 
their space complexity is O(1). Since the Trie saves each character as a node, it's space complexity is O(n).  
