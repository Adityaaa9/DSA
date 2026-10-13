class Solution:
    # Function to get the sum of highest
    # and lowest frequency in array
    def sumHighestAndLowestFrequency(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        # Variable to store maximum 
        # and minimum frequency
        maxFreq = 0
        minFreq = n
        
        # HashMap
        mpp = {}
        
        # Iterating on the array
        for num in nums:
            # Updating hashmap
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1
                
        # Iterate on the map
        for freq in mpp.values():
            # Update maximum and 
            # minimum frequencies
            maxFreq = max(maxFreq, freq)
            minFreq = min(minFreq, freq)
            
        # Return the required sum
        return maxFreq + minFreq

# Test the solution
if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to get the sum of highest
    # and lowest frequency in array
    ans = sol.sumHighestAndLowestFrequency(nums)
    
    print(f"The sum of highest and lowest frequency in the array is: {ans}")
# https://app.notion.com/p/Optimal-3f8f79cdb3f98086bc21da26220a946b