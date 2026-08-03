class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1
    
        while bottom <= top:
            mid = int((top-bottom)/2) + bottom
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                l = 0
                r = len(matrix[mid]) - 1
                while l <= r:
                    cent = int((r-l)/2) + l
                    if matrix[mid][cent] < target:
                        l = cent + 1
                    elif matrix[mid][cent] > target:
                        r = cent -1
                    else:
                        return True
                return False
            elif matrix[mid][0] > target:
                top = mid - 1
            else:
                bottom = mid + 1
        
        return False