from typing import List

class Solution:
    # Function to remove duplicates from the list
    def removeDuplicates(self, nums: List[int]) -> int:
      
        
        # Initialize pointer for unique elements
        i = 0
        
        # Iterate through the list
        for j in range(1, len(nums)):
            """ If current element is different 
            from the previous unique element"""
            if nums[i] != nums[j]:
                
                """ Move to the next position in 
                the list for the unique element"""
                i += 1
                
                """ Update the current position 
                with the unique element"""
                nums[i] = nums[j]
        
        # Return the number of unique elements
        return i + 1

# Main function to test the implementation
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3, 3]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call removeDuplicates to remove duplicates from nums
    k = solution.removeDuplicates(nums)
    
    print("The list after removing duplicate elements is ")
    for i in range(k):
        print(nums[i], end=" ")
    print()


# https://app.notion.com/p/Optimal-40df79cdb3f9802d92a7d76115d8c458