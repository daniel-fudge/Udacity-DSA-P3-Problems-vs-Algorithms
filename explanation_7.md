# Problem 7 of the Data Structures Project
This problem follows a set Workbook from Udacity discussed in problem 5 [here](explanation_5.md). It also has the 
strategy and code skeleton defined [here](https://learn.udacity.com/nanodegrees/nd256/parts/cd1887/lessons/032713d7-07e0-468f-8393-7b34bf2899e7/concepts/93275178-63ff-4666-88a3-e66e6e29eb2f). 
The primary difference between this question and question 5, is each node of the trie represents a path between the 
"\"'s in the full path. The `word_ending` bool flag that denoted a word ending is also replaced by a handler.   
As discussed in the 5th [explanation](explanation_5.md), Trie data structures have the advantage of not having to repeat 
common prefixes, unlike a simple dictionary of paths and associated handlers.   
Note user test set 2 and 3, demonstrate the bonus and "more bonus" capabilities.

## Time Efficiency
In the following discussion, "c" is the number of characters in the full path and "n" is the 
number words in the full path separated by "/" characters. Within the trie, each of these "n" words are nodes. Since "c"
equals "n" times the average word, "n" < "c". If "n" became very large, O(n) ~ O(c). 

### RouteTrieNode.__init__
This method simply sets the node attributes so has a O(1) time complexity.

### RouteTrieNode.insert
This method simply creates and adds a child node for the given character so has a O(1) time complexity.

### RouteTrie.__init__
This method simply sets the trie attributes so has a O(1) time complexity.

### RouteTrie.insert
This method has to split the given full path by the "/" character, which requires a full traversal through all "c" 
characters in the given path, therefore the time complexity is O(c). It also adds each of the resulting words to the 
trie as a node with a time complexity of O(n). Combined this gives O(c + n) ~ O(n).

### RouteTrie.find
Similar to the `RouteTrie.insert` method, this method has to split the given path of "c" characters on the "/" character 
into "n" words (nodes) and then check if these nodes are in the Trie. Therefore, the time complexity is O(c + n) ~ O(n). 

### Router.__init__
This method simply sets the router attributes so has a O(1) time complexity.

### Router.add_handler
This method calls the `RouteTrie.insert` method so as discussed above has a time complexity of O(c + n) ~ O(n).

### Router.lookup
This method calls the `RouteTrie.find` method so as discussed above has a time complexity of O(c + n) ~ O(n).


## Space Efficiency
There are no recursions in this implementation, so we do not have a call stack to consider. The primary space complexity 
drivers are the given full path of "c" characters and the resulting "n" nodes in the trie.

### RouteTrieNode.__init__
This method simply sets the node attributes so has a O(1) space complexity.

### RouteTrieNode.insert
This method simply creates and adds a child node for the given character so has a O(1) space complexity.

### RouteTrie.__init__
This method simply sets the trie attributes so has a O(1) space complexity.

### RouteTrie.insert
This method has to split the given full path by the "/" character into "n" words and adds each of the resulting words to 
the trie as a node. This gives a space complexity of O(n).

### RouteTrie.find
Similar to the `RouteTrie.insert` method, this method has to split the given path of "c" characters on the "/" character 
into "n" words (nodes) and then check if these nodes are in the Trie. Therefore, the space complexity is O(n). 

### Router.__init__
This method simply sets the router attributes so has a O(1) space complexity.

### Router.add_handler
This method calls the `RouteTrie.insert` method so as discussed above has a space complexity of O(n).

### Router.lookup
This method calls the `RouteTrie.find` method so as discussed above has a space complexity of O(n).
