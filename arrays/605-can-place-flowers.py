'''
    TC: O(n),
    SC: O(1)

    Just do exactly what the problem is asking: check the left and right elements and see if you plant
    or not. Just make sure to check for the first and last index (edge case).

    There is another solution where you don't have to check the first and last index as you append a 0
    to the beginning and end, but that makes the SC: O(n). 
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possiblePlants = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftEmpty = False
                rightEmpty = False

                if i == 0 or flowerbed[i-1] == 0:   # if it's the first element, or checking the left side
                    leftEmpty = True
                if i == len(flowerbed)-1 or flowerbed[i+1] == 0:    # if it's the last element, or checking the right side
                    rightEmpty = True

                if leftEmpty and rightEmpty:
                    flowerbed[i] = 1
                    possiblePlants += 1


        if possiblePlants >= n:
            return True
        else:
            return False 
