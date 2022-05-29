# Problem 5 of the Data Structures Project
This problem follows a set Workbook from Udacity that was completed and saved [here](Trie.ipynb) as directed in the 
Udacity problem 5 description.   
This solution implements a Trie to represent a listing of words. The advantage of the Trie over a standard set is 
common prefixes are shared, making the time and space complexity O(n), where n is the unique character position. For 
instance, "i", "it", "item" and "items" together only have n = 5 nodes in the Trie, each with a single character. If 
stored as a set, it would have 4 elements, with a total of 12 characters.    
Note that "cook" has only 3 unique characters but n = 4 unique character positions.

## Time Efficiency
Please note that user test set 5 confirms the O(n) insert and find time complexity with words with 10^5, 10^6 and 10^7 
characters. User test 6 confirms the O(n) suffixes time complexity with words of 10, 100 and 1000 characters. A much 
smaller n value had to be used for the suffixes check due to the recursion within the "suffixes" method.

### TrieNode.__init__
This method simply sets the node attributes so has a O(1) time complexity.

### TrieNode.insert
This method simply creates and adds a child node for the given character so has a O(1) time complexity.

### TrieNode.collect_suffixes
This is a recursive method called by `TrieNode.suffixes` that traverses the full trie so has a time complexity of O(n).

### TrieNode.suffixes
As mentioned above, this calls the recursive `TrieNode.collect_suffixes` that traverses the full trie so has a time 
complexity of O(n).  

### Trie.__init__
This method simply sets the trie attributes so has a O(1) time complexity.

### TrieNode.insert
This method inserts a node for every n characters in the given word so has a O(n) time complexity.

### TrieNode.find
This method traverses the trie for every n characters is the given prefix has a O(n) time complexity.

## Space Efficiency
Since find and insert method of the trie do not build any data structures or use recursive functions (no call stack), 
their space complexity is O(1). Since the Trie saves each character as a node, it's space complexity is O(n). 

### TrieNode.__init__
This method simply sets the node attributes so has a O(1) space complexity.

### TrieNode.insert
This method simply creates and adds a child node for the given character so has a O(1) space complexity.

### TrieNode.collect_suffixes
This is a recursive method called by `TrieNode.suffixes` that traverses the full trie and saves the suffixes to a list 
has a space complexity of O(s * m), where s is the number of found suffixes and m is the average suffix length. 
This method is also recursive with a "n" sized call stack, so it has a space complexity of O(n).    
Therefore, the total space complexity will be O(n + s*m). 

### TrieNode.suffixes
As mentioned above, this calls the recursive `TrieNode.collect_suffixes` that traverses the full trie so has a space 
complexity of O(n + s*m). 

### Trie.__init__
This method simply sets the trie attributes so has a O(1) space complexity.

### TrieNode.insert
This method inserts a node for every n characters in the given word so has a O(n) space complexity.

### TrieNode.find
This method traverses the trie for every n characters is the given prefix has a O(n) space complexity.
