class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:

            if self.binar_serch(row, target):
                return True

        return False
        
    def binar_serch(self, array: list[int], target: int) -> bool:
        l, r = 0, len(array) - 1

        while l <= r:
            m = (l + r) // 2
            
            if array[m] == target:
                return True
            elif array[m] > target:
                r = m - 1
            elif array[m] < target:
                l = m + 1

        return False