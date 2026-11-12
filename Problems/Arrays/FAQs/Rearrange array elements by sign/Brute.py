class Solution:
    # Function to rearrange the given array by signs
    def rearrangeArray(self, nums):
        n = len(nums)
        
        """ Define 2 vectors, one for storing positive 
        and other for negative elements of the array."""
        pos = []
        neg = []
  
        # Segregate the array into positives and negatives.
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
  
        # Positives on even indices, negatives on odd.
        for i in range(n // 2):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]
        
        # Return the result
        return nums

if __name__ == "__main__":
    A = [1, 2, -4, -5]
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.rearrangeArray(A)
    
    # Print the result
    print(" ".join(map(str, ans)))


# https://app.notion.com/p/Brute-416f79cdb3f9806fa967fbe72267516f