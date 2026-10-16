class Solution:
    # Method to find the longest common prefix in a list of strings
    def longestCommonPrefix(self, strs):
        # Edge case: empty list
        if not strs:
            return ""
        
        # Traverse character by character using the first string as reference
        for i in range(len(strs[0])):
            
            # Current character from the first string
            ch = strs[0][i]
            
            # Compare this character with the same index in all other strings
            for j in range(1, len(strs)):
                
                # If the current string ends or characters do not match, return prefix
                if i == len(strs[j]) or strs[j][i] != ch:
                    return strs[0][:i]
        
        # If all characters match, the first string itself is the longest common prefix
        return strs[0]

# Test the longestCommonPrefix method
if __name__ == "__main__":
    solution = Solution()
    input_strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(input_strs)
    print("Longest Common Prefix:", result)  # Output: "fl"

# https://app.notion.com/p/Vertical-scan-3fbf79cdb3f980a5ba01c87661ec3e4c