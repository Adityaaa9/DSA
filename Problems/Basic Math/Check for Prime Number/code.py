class Solution:
    def isPrime(self, n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

if __name__ == "__main__":
    n = 7
    
    sol = Solution()
    ans = sol.isPrime(n)
    
    if ans:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

# https://app.notion.com/p/Check-for-Prime-Number-3eaf79cdb3f9805a8fd9fd29e6873523