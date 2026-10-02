class Solution:
    # Function to check if an array is sorted
    def arraySortedOrNot(self, arr, n):
        # Iterate through the array
        for i in range(n - 1):
            
            # Compare each element with the next one
            if arr[i] > arr[i + 1]:
                
            # If any element is greater than the next one,
            # the array is not sorted  
                return False  
                
        # If no such pair is found, array is sorted
        return True  

# Driver code

# Creating an instance of solution class
solution = Solution()
arr = [1, 2, 3, 4, 5]
n = len(arr)

# Function call to check if the array is sorted
sorted = solution.arraySortedOrNot(arr, n)
if sorted:
    print("Array is sorted.")
else:
    print("Array is not sorted.")

# https://app.notion.com/p/Optimal-3edf79cdb3f980149078cc096066148e