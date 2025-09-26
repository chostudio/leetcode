# Last updated: 9/25/2025, 7:47:30 PM
class ListNode:
    def __init__(self, key, val):
        self.key = key # okay the reason you need the key value in the node is bc you need to delete the key from the hashmap if the # of keys exceed capacity. and so you would remove the left most actual value AND grab the key stored in that node to delete it from the hashmap too
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # u aint gonna believe me but it's a hashmap and doubly linkedlist and you gotta code the linkedlist class for O(1) time for everything.
    # there is only one value per key (hashmap). but the cache takes in and accounts for all the keys and value pairs from least to most recent. 
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hashmaps of pointers to nodes in a doubly linkedlist aint that crazy

        # the doubly linkedlist init. it's kind of like hugging the actual nodes inbetween them lol
        self.left = ListNode(0, 0) # doesnt matter what values u put here but you need to put something
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node): # pass in the reference to the node. reminder thaty you need to pass in self here too. why?
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev # poof magic the node is gone from the list bc the adj nodes dont point to it anymore. and there will always be a prev and next node surrounding it bc we have l and r nodes at the two ends 
    
    def insert(self, node): # only at right pointer
        prev = self.right.prev
        prev.next = node
        self.right.prev = node # updated the two other nodes. and now update node to point back at them bc it's a doubly linked list
        node.next = self.right
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # update position in list
            self.remove(self.cache[key]) # reminder that you need to do self. b4 calling function names
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove it so we can move it to the front
            self.remove(self.cache[key])
        # whether it's in or not made yet we want to move the node to the front of the used list anyways.
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next # save the node we're deleting to get the key to delete from the hashmap too
            self.remove(lru)
            del self.cache[lru.key]
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)