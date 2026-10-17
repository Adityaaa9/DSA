class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
   # Strings must be same length to be rotations of each other
        if len(s) != len(goal):
            return False  
        # Try all possible rotations of s
        for i in range(len(s)):
            rotated = s[i:] + s[:i]  # Create a new rotation
            if rotated == goal:
                return True  
        return False  

# Test cases
sol = Solution()
print(sol.rotateString("abcde", "cdeab"))  # Output: True
print(sol.rotateString("abcde", "abced"))  # Output: False

# https://app.notion.com/p/Brute-3fcf79cdb3f9807a9417f2571c69d992