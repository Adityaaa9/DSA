from typing import List

class Solution:
    """ Function to find two indices in the array `nums`
       such that their elements sum up to `target`.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Size of the nums array
        n = len(nums)
        
        # List to store indices of two numbers
        ans = [-1, -1]
        
        # 2D list to store [element, index] pairs
        eleIndex = []
        for i in range(len(nums)):
            eleIndex.append([nums[i], i])
        
        """ Sort eleIndex by the first
        element in ascending order"""
        eleIndex.sort(key=lambda x: x[0])

        """ Two pointers: one starting 
         from left and one from right"""
        left, right = 0, n - 1

        while left < right:
            """ Calculate sum of elements
            at left and right pointers"""
            sum_val = eleIndex[left][0] + eleIndex[right][0]

            if sum_val == target:
                
                """ If sum equals target,
                store indices and return"""
                ans[0] = eleIndex[left][1]
                ans[1] = eleIndex[right][1]
                return ans
                
            elif sum_val < target:
                
                """ If sum is less than target,
                move left pointer to the right"""
                left += 1
                
            else:
                
                """ If sum is greater than target,
                move right pointer to the left"""
                right -= 1

        # If no such pair found, return [-1, -1]
        return ans

if __name__ == "__main__":
    nums = [2, 6, 5, 8, 11]
    target = 14

    # Create an instance of Solution class
    sol = Solution()

    ans = sol.twoSum(nums, target)

    # Print the result
    print(f"Indices of the two numbers that sum up to {target} are: [{ans[0]}, {ans[1]}]")

# https://app.notion.com/p/Optimal-41df79cdb3f980dabd44c074e2be6555