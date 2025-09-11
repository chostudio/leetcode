# Last updated: 9/11/2025, 12:31:37 PM
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = defaultdict(int)
        for i in words:
            hashmap[i] += 1
        freq = 0
        arr = [[] for i in range((len(words)+2))]
        print(arr)
        print(hashmap)
        # bucket sort
        for key, val in hashmap.items():
            print(hashmap[key])
            arr[hashmap[key]].append(key)
            arr[hashmap[key]].sort()
        ans = []
        print(arr)
        # go backwards
        for i in range(len(arr)-1, 0, -1):
            # go forward within the
            print(i)
            if arr[i]:
                for j in arr[i]:
                    print(j)
                    ans.append(j)
                    k -= 1
                    if k == 0:
                        break
            if k == 0:
                    break
        return ans
