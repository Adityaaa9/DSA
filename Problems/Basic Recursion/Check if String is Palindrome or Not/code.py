class Solution:
    def palindromeCheck(self, s: str) -> bool:
        # Call the recursive helper method with initial indices
        return self.isPalindrome(s, 0, len(s) - 1)
    
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        # Base Case: If the start index is greater than or equal to the end index
        if left >= right:
            return True
        # Check if characters at the current positions are the same
        if s[left] != s[right]:
            return False  # Characters do not match, so it's not a palindrome
        # Recur for the next set of characters
        return self.isPalindrome(s, left + 1, right - 1)
    
# Main method to test the palindromeCheck function
if __name__ == "__main__":
    solution = Solution()
    print(solution.palindromeCheck("hannah"))  # Output: True
    print(solution.palindromeCheck("aabbaaa"))  # Output: False
    print(solution.palindromeCheck("aba"))      # Output: True

# https://app.notion.com/p/Check-if-String-is-Palindrome-or-Not-405f79cdb3f98069bfd1c9a2c583b35c