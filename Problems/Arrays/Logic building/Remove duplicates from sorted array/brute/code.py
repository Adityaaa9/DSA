class Solution:
    # Function to remove duplicates from the array
    def removeDuplicates(self, nums):
        
        # Set data structure to store unique elements
        s = set()
        
        # Add all elements from array to the set
        for val in nums:
            s.add(val)
        
        # Get the sorted list of unique elements
        sorted_unique = sorted(s)
        
        # Copy unique elements from sorted list to array
        for j in range(len(sorted_unique)):
            nums[j] = sorted_unique[j]
        
        # Return the number of unique elements
        return len(sorted_unique)

# Helper function to print first n elements of the array
def printArray(nums, n):
    for i in range(n):
        print(nums[i], end=" ")
    print()

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3, 3]
    
    print("Original Array: ", end="")
    printArray(nums, len(nums))
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Function call to remove duplicates from array
    k = sol.removeDuplicates(nums)
    
    print("Array after removing the duplicates: ", end="")
    printArray(nums, k)


# https://app.notion.com/p/Brute-40df79cdb3f9801291a2e497816ee5a6