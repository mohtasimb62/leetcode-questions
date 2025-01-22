from typing import List


'''
Brute Force:
    TC: O(max-min+1) * O(n)
    SC: O(1)

    Find the lowest and highest in the list as the days will be between that. Calculate how many bouquets
    you can make for each of them and return as soon as you find the day where you can make m bouquets
    as you need the minimum.
'''
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        minDay = min(bloomDay)
        maxDay = max(bloomDay)

        for i in range(minDay, maxDay+1):
            bouquets = self.flowersBloomed(bloomDay, m, k, i)

            if bouquets >= m:
                return i
            
        return -1

    def flowersBloomed(self, arr, m, k, day):
        total = 0
        count = 0

        for i in range(0, len(arr)):
            if arr[i] <= day:
                count += 1
            else:
                total += count // k     # to find the number of adjacent bouquets possible
                count = 0

        total += count // k

        return total
    

'''
'''