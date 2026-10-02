class Solution:
    def arraySortedOrNot(self, arr, n):
        # Iterate through each element
        for i in range(n - 1):
            # Compare with every subsequent element
            for j in range(i + 1, n):
                # If any element is out of order, return False
                if arr[i] > arr[j]:
                    return False
        # All elements are in order
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

# https://app.notion.com/p/Brute-3edf79cdb3f9806583e6ee931ce36241