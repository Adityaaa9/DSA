class Solution:
    def reverseArray(self, nums):
        # Call the helper function to reverse the array
        self.reverse(nums, 0, len(nums) - 1) 
        # Return the reversed array 
        return nums  

    def reverse(self, nums, left, right):
        if left >= right:
            return 
        # Swap the elements        
        nums[left], nums[right] = nums[right], nums[left]  
        # Recursive call with updated pointers
        self.reverse(nums, left + 1, right - 1)  

# Main method for testing the reverseArray function
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]  
    result = solution.reverseArray(nums)  
    print(result)  # Print the reversed array

# https://app.notion.com/p/Reverse-an-array-2-407f79cdb3f980daad5cd581881c89ca