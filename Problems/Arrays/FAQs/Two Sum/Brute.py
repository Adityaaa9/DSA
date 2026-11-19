from typing import List

class Solution:
    """
    Function to find two indices in the array `nums`
    such that their elements sum up to `target`.
    """
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        # Create ans list to store the indices
        ans = [0, 0]
        for i in range(n):
            for j in range(i + 1, n):
                
                """If nums[i] + nums[j] is equal to target
                put i and j in ans"""
                if nums[i] + nums[j] == target:
                    ans[0] = i
                    ans[1] = j
                    return ans
        
        # Return [-1, -1] if no such pair is found
        return [-1, -1]

if __name__ == "__main__":
    n = 5
    nums = [2, 6, 5, 8, 11]
    target = 14
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Call the twoSum method to find the indices
    ans = sol.twoSum(nums, target)
    
    # Print the result
    print(f"This is the answer: [{ans[0]}, {ans[1]}]")

# https://app.notion.com/p/Brute-41df79cdb3f98021bf1dc5b85d20bbb1