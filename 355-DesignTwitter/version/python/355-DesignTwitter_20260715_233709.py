# Last updated: 7/15/2026, 11:37:09 PM
1class Twitter:
2
3    def __init__(self):
4        self.posts = defaultdict(list)
5        self.follows = defaultdict(set) # set for O(1) add remove, check
6        self.t = 0
7
8    def postTweet(self, userId: int, tweetId: int) -> None:
9        self.posts[userId].append((self.t, tweetId))
10        self.t -= 1
11
12    def getNewsFeed(self, userId: int) -> List[int]:
13        heap = []
14        for poster in self.follows[userId]:
15            # grab the most recnet post (-time, tweetid) from the person that user follows
16            # grab latest
17            if len(self.posts[poster]) != 0:
18                time, tweetid = self.posts[poster][-1]
19                heapq.heappush(heap, (time, tweetid, poster, len(self.posts[poster])-1))
20        
21        # you know what's crazy? there's an edge case where the user needs to SEE THEIR OWN POSTS TOO
22        if len(self.posts[userId]) != 0:
23            time, tweetid = self.posts[userId][-1]
24            heapq.heappush(heap, (time, tweetid, userId, len(self.posts[userId])-1))
25
26        ans = []
27        # if less than 10 in heap then quit out, otherwise stop when 10
28        print(heap)
29        while heap and len(ans) < 10:
30            # get most recnet post out of all of most recnet post from posters they follow
31            time, tweetid, poster, index = heapq.heappop(heap)
32            ans.append(tweetid)
33            if index > 0:
34                nexttime, nexttweetid = self.posts[poster][index - 1]
35                heapq.heappush(heap, (nexttime, nexttweetid, poster, index - 1))
36        return ans
37
38    def follow(self, followerId: int, followeeId: int) -> None:
39        self.follows[followerId].add(followeeId)
40
41    def unfollow(self, followerId: int, followeeId: int) -> None:
42        if followeeId in self.follows[followerId]:
43            self.follows[followerId].remove(followeeId)
44
45
46# Your Twitter object will be instantiated and called as such:
47# obj = Twitter()
48# obj.postTweet(userId,tweetId)
49# param_2 = obj.getNewsFeed(userId)
50# obj.follow(followerId,followeeId)
51# obj.unfollow(followerId,followeeId)