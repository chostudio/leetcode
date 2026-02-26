# Last updated: 2/26/2026, 1:39:27 PM
1class AuctionSystem:
2
3    def __init__(self):
4        self.users = defaultdict(dict) # a user's bids
5        self.items = defaultdict(list) # heap bids
6
7    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
8        self.users[userId][itemId] = bidAmount
9        heapq.heappush(self.items[itemId], (-bidAmount, -userId))
10
11    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
12        self.users[userId][itemId] = newAmount
13        heapq.heappush(self.items[itemId], (-newAmount, -userId))
14        
15
16    def removeBid(self, userId: int, itemId: int) -> None:
17        del self.users[userId][itemId]
18        # we check heap at getHIghestBidder runtime
19
20    def getHighestBidder(self, itemId: int) -> int:
21        # technically, we don't need this if statement. We could just return 1 at the end. But I think this is a nice catch here 
22        if itemId not in self.items:
23            return -1
24        # else exists, remember to negate user id
25        while self.items[itemId]: # while there's things inside:
26            bidAmount, userId = heapq.heappop(self.items[itemId])
27
28            bidAmount = abs(bidAmount)
29            userId = abs(userId)
30            # check if it exists first
31            # this is the correct syntax to check if inside double dict
32            if userId in self.users and itemId in self.users[userId] and self.users[userId][itemId] == bidAmount:
33                # put back into heap first lol
34                heapq.heappush(self.items[itemId], (-bidAmount, -userId))
35                return userId
36        return -1 # we still need to return -1 at the end because there is the possibility that there are things inside of the heap, but none of the values are accurate anymore 
37        # we technically dont need to remove any further values form the heap (aka clean up the entire heap) but if we dont delete then it'll take up memory space, something to note.
38
39
40# Your AuctionSystem object will be instantiated and called as such:
41# obj = AuctionSystem()
42# obj.addBid(userId,itemId,bidAmount)
43# obj.updateBid(userId,itemId,newAmount)
44# obj.removeBid(userId,itemId)
45# param_4 = obj.getHighestBidder(itemId)