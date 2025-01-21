import math
from typing import List

'''
Brute force:
    TC: O(n^2),
    SC: O(1)

    We are finding the max element (a), looping a times, iterating the whole list (n). This results in a
    TLE. 

    Essentially, the trick here is to find the highest rate possible. In this case, it's the biggest
    element in the list. Then for each of the hours possible (from 1 to the max element), we calculate
    how long it takes to eat all the bananas and if the time taken is equal to h, return that hour.
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxElement = max(piles)

        for i in range(1, maxElement+1):
            currRate = self.rate(piles, i)

            if currRate == h:
                return i

        return 0

    def rate(self, arr, k):
        totalHours = 0
        for i in range(0, len(arr)):
            totalHours += math.ceil(arr[i] / k)
        
        print(totalHours)

        return totalHours
    

'''
Optimal approach:
    TC: O(n) * O(logn),
    SC: O(1)

    Instead of calculating the time taken for every speed, find the speed using binary search. At this
    point, it's just finding the minimum in a list.
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxElement = max(piles)
        low = 1
        high = maxElement
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            currRate = self.rate(piles, mid)

            if currRate <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def rate(self, arr, k):
        totalHours = 0
        for i in range(0, len(arr)):
            totalHours += math.ceil(arr[i] / k)
        
        print(totalHours)

        return totalHours
        