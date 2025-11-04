# Last updated: 11/3/2025, 9:58:35 PM
class Solution:
    def reorganizeString(self, s: str) -> str:
        # or is it find max elmeent, if that elemnt has no more than half, compared to total, then it is possible
        # find max element then see if you can put the rest in every other slot. maybe heap. doesnt have to be max elmeent only but heap every other? heap always place mot common letter? alternate between them how? jsut don't ptut he same last letter so go to 2nd most leter in heap?
        # hashmap to get freq then put in heap max freq
        freq = Counter(s)
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
        
        arr = []
        while heap:
            # always get the most freq val unless it's the same one as the last one
            if len(arr) == 0 or heap[0][1] != arr[-1]:
                freq, key = heapq.heappop(heap)
                arr.append(key)
                freq += 1
                if freq != 0: # bc negative
                    heapq.heappush(heap, (freq, key))
            elif heap[0][1] == arr[-1] and len(heap) >= 2: # heap[0][1] == arr[-1]
                freq, key = heapq.heappop(heap)
                secondfreq, secondkey = heapq.heappop(heap)
                arr.append(secondkey)
                secondfreq += 1
                if secondfreq != 0: # bc negative
                    heapq.heappush(heap, (secondfreq, secondkey))
                heapq.heappush(heap, (freq, key)) # add back other one
            else: # impossbile return false
                return ""
        return "".join(arr)