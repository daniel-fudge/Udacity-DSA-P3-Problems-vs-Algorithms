# Problem 7 of the Data Structures Project
This problem follows a set Workbook from Udacity discussed in problem 5 [here](explanation_5.md). It also has the 
strategy and code skeleton defined [here](https://learn.udacity.com/nanodegrees/nd256/parts/cd1887/lessons/032713d7-07e0-468f-8393-7b34bf2899e7/concepts/93275178-63ff-4666-88a3-e66e6e29eb2f). 
The primary difference between this question and question 5, is each node of the trie represents a path between the 
"\"'s in the full path. The `word_ending` bool flag that denoted a word ending is also replaced by a handler.   
As discussed in the 5th [explanation](explanation_5.md), Trie data structures have the advantage of not having to repeat 
common prefixes, unlike a simple dictionary of paths and associated handlers.   
Note user test set 2 and 3, demonstrate the bonus and "more bonus" capabilities.

## Time Efficiency
In practice, the number of nodes "n" in this trie is will never become large enough to make the time or space complexity 
a major design concern.   
Since find and insert method of the trie completely traverse the given full path, their time complexity is O(n). 

## Space Efficiency
Since find and insert method of the trie do not build any data structures or use recursive functions (no call stack), 
their space complexity is O(1).   
Since the Trie saves each path as a node, it's space complexity is O(n).  
