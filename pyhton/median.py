from typing import List

class Solution:
    # list - sorted array with not repeated elements
    def findMedian(self, list: List[int]):
        l = len(list)
        i = l // 2
        if l % 2 != 0:
            return list[i]
        else:
            #leftMax = max(list[0:i])
            #rightMin = min(list[i:l])
            #return (leftMax + rightMin) // 2
            return (list[i] + list[i+1]) / 2


assert Solution().findMedian([1]) == 1.0
assert Solution().findMedian([1, 2, 3]) == 2.0
assert Solution().findMedian([1, 2, 3, 4]) == 2.5