from typing import List

'''
Brute Force:
    TC: O(sum(n)) * O(max(n)) * O(n)
    SC: O(1)

    Find the range (the starting and ending number) and that will be the range of the capacity. For each 
    capacity, see if it can be shipped within `days`. Return the capacity as soon as you find it.
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowest = max(weights)       # to ensure that the heaviest element can be shipped
        highest = sum(weights)      # to ensure that everything can be shipped in 1 day
        ans = -1

        for i in range(lowest, highest+1):
            daysTaken = self.calculateDays(weights, i)

            if daysTaken <= days:
                ans = i
                return ans

        return ans

    def calculateDays(self, arr, capacity):
        days = 1
        currLoad = 0

        for i in range(0, len(arr)):
            if currLoad + arr[i] <= capacity:
                currLoad += arr[i]
            else:
                days += 1
                currLoad = arr[i]

        return days