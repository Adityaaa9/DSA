from typing import List

class Solution:
    # Function to find triplets having sum equals to target
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # List to store the triplets that sum up to target
        ans = []
        
        n = len(nums)
        
        # Sort the input array nums
        nums.sort()
        
        # Iterate through the array to find triplets
        for i in range(n):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers approach
            j = i + 1
            k = n - 1
            
            while j < k:
                sum_val = nums[i] + nums[j] + nums[k]
                
                if sum_val < 0:
                    j += 1
                elif sum_val > 0:
                    k -= 1
                else:
                    # Found a triplet that sums up to target
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    
                    # Skip duplicates
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return ans

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    
    # Create an instance of Solution class
    sol = Solution()

    ans = sol.threeSum(nums)
    
    # Print the result
    for triplet in ans:
        print(f"[{', '.join(map(str, triplet))}]")


# https://app.notion.com/p/Optimal-41ef79cdb3f9806eba38f6620adfafa8