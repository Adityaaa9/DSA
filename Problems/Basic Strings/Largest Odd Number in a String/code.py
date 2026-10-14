class Solution:
    # Function to find the largest odd number 
    # that is a substring of given string 
    def largeOddNum(self, s: str) -> str:
        ind = -1
        
        # Iterate through the string from the end to beginning
        for i in range(len(s) - 1, -1, -1):
            # Break if an odd digit is found
            if (int(s[i]) % 2) == 1:
                ind = i
                break
        
        # Skipping any leading zeroes
        i = 0
        while i <= ind and s[i] == '0':
            i += 1
        
        # Return the largest odd number substring
        return s[i:ind + 1]

# Driver code
solution = Solution()
num = "504"
result = solution.largeOddNum(num)
print("Largest odd number:", result)

# https://app.notion.com/p/Largest-Odd-Number-in-a-String-3f9f79cdb3f980dca915d60c4c4453e3