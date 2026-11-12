from typing import List

class Solution:
    # Function to print matrix in spiral manner
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        # Number of rows
        n = len(matrix)

         # Number of columns
        m = len(matrix[0])
        
        # Initialize pointers for traversal
        top, left = 0, 0
        bottom, right = n - 1, m - 1
        
        # Traverse the matrix in spiral order
        while top <= bottom and left <= right:
            # Traverse from left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            
            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            
            # Traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        
        #Return the ans
        return ans

# Test the solution
if __name__ == "__main__":
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    # Create an instance of the Solution class
    finder = Solution()
    
    # Get spiral order using class method
    ans = finder.spiralOrder(mat)

    print("Elements in spiral order are:", ans)

# https://app.notion.com/p/Print-the-matrix-in-spiral-manner-416f79cdb3f9807392abe63b193fca4a