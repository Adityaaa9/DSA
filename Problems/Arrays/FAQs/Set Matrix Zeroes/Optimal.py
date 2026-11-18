class Solution:
    # Method to set entire rows and columns to 0 if a 0 is found in the matrix
    def setZeroes(self, matrix):
        # Number of rows
        m = len(matrix)
        
        # Number of columns
        n = len(matrix[0])
        
        # Flag to check if the first row needs to be zeroed
        firstRowZero = False
        
        # Flag to check if the first column needs to be zeroed
        firstColZero = False
        
        # Step 1: Check if the first column needs to be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True
                break
        
        # Check if the first row needs to be zeroed
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True
                break
        
        # Step 2: Use first row and first column to mark zero rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    # Mark the first column of the current row
                    matrix[i][0] = 0
                    
                    # Mark the first row of the current column
                    matrix[0][j] = 0
        
        # Step 3: Set matrix elements to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 4: Zero the first row if needed
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Step 5: Zero the first column if needed
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    sol = Solution()
    
    # Example matrix:
    # 1 2 3
    # 4 0 6
    # 7 8 9
    matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    
    sol.setZeroes(matrix)
    
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()


# https://app.notion.com/p/Optimal-41cf79cdb3f9802bae90d18e67cfa818