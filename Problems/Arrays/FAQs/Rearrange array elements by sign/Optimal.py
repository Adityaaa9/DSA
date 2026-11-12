from typing import List
class Solution:
    #Function to rearrange elements by their sign
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize a result vector of size n
        ans = [0] * n  
        
        # Initialize indices for positive and negative elements
        posIndex, negIndex = 0, 1  
        
        # Traverse through each element in nums
        for i in range(n):
            if nums[i] < 0:
                
                """ If current element is negative, 
                place it at the next odd index in ans"""
                ans[negIndex] = nums[i]
                # Move to the next odd index
                negIndex += 2
                
            else:
                ans[posIndex] = nums[i]

                # Move to the next even index
                posIndex += 2
        
        # Return the rearranged array
        return ans

if __name__ == "__main__":
    A = [1, 2, -4, -5]
    
    # Create an instance of the Solution class
    sol = Solution()
    ans = sol.rearrangeArray(A)
    
    # Print the rearranged array
    print(" ".join(map(str, ans)))

# https://app.notion.com/p/Optimal-416f79cdb3f980369d57d6bf529ff257