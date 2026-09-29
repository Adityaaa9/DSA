class Solution:
    def primeUptoN(self, n):
        if n < 2:
            return 0
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        return sum(is_prime)

# Input number
n = 6
 
# Creating an instance of Solution class
sol = Solution()
 
# Function call to get count of all primes till n
ans = sol.primeUptoN(n)
 
print("The count of primes till", n, "is:", ans)

# https://app.notion.com/p/Count-of-Prime-Numbers-till-N-3eaf79cdb3f9805692d2f4918ace4af3