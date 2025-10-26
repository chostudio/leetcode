# Last updated: 10/26/2025, 4:03:03 PM
class Node:
    def __init__(self):
        self.child = {} # holds letter: node
        self.wordEnd = False # boolean T or F init at false first

class Trie:

    def __init__(self):
        self.root = Node() # the first root is nothing, then follows by firs letters

    def insert(self, word: str) -> None:
        # if it's not there then we nee to add it
        #if it's already there or we just added it then we move ont the next char to add it
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = Node()
            curr = curr.child[char] # then update by moving curr
        curr.wordEnd = True # then at last letter make sure to set end as in a word ends here at this letter

    # main diff between last two is search but is last char end word
    def search(self, word: str) -> bool:
        curr = self.root # alwasy starting off at the root node
        for char in word:
            if char not in curr.child:
                return False 
                # if next letter not in then false
            curr = curr.child[char]
        return curr.wordEnd # else we make it through the entire word BUT not guarenteed that this is the "end" of a word we previously put in so we have to check if this is a legit word end and not just a prefix any kind

    def startsWith(self, prefix: str) -> bool:
        curr = self.root # alwasy starting off at the root node
        for char in prefix:
            if char not in curr.child:
                return False 
                # if next letter not in then false
            curr = curr.child[char]
        return True # else we make it thru the entire prefix then all good


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)