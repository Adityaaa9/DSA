class Solution:
    def factorial(self, n):
        # Base case: factorial of 0 or 1 is 1
        if n<= 1:
            return 1
        # Recursive case: n * factorial of n-1
        return n* self.factorial(n- 1)

if __name__ == "__main__":
    solution = Solution()
    N = 5 # Example input
    print(f"Factorial of {N} is {solution.factorial(N)}")

# https://app.notion.com/p/Factorial-of-a-Given-Number-400f79cdb3f98063943cf01d9cc79a3a