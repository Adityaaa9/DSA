from typing import List

class Solution:
    """ Function to find two indices in the array `nums`
       such that their elements sum up to `target`.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store (element, index) pairs
        mpp = {}
        
        # Length of the nums list
        n = len(nums)
        
        for i in range(n):
            # Current number in the list
            num = nums[i]
            
            # Number needed to reach the target
            more_needed = target - num

            # Check if complement exists in dictionary
            if more_needed in mpp:
                """ Return the indices of the two
                numbers that sum up to target"""
                return [mpp[more_needed], i]

            """Store current number and 
            its index in dictionary"""
            mpp[num] = i
        
        # If no such pair found, return [-1, -1]
        return [-1, -1]


if __name__ == "__main__":
    nums = [2, 6, 5, 8, 11]
    target = 14

    # Create an instance of Solution class
    sol = Solution()
    
    # Call the twoSum method from Solution class
    ans = sol.twoSum(nums, target)

    # Print the result
    print(f"Indices of the two numbers that sum up to {target} are: [{ans[0]}, {ans[1]}]")

# https://app.notion.com/p/Better-41df79cdb3f980b6b618c67ac1882a0f