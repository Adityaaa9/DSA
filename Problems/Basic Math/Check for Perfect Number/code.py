class Solution:
    def isPerfect(self, n: int) -> bool:
        if n <= 1:
            return False

        total = 1

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                total += i

                if i != n // i:
                    total += n // i

        return total == n

# Input number
n = 6
 
# Creating an instance of Solution class
sol = Solution()
 
# Function call to find whether the given number is perfect or not
ans = sol.isPerfect(n)
 
if ans:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")

# https://app.notion.com/p/Check-for-Perfect-Number-3eaf79cdb3f980b0ac71c4151a3c2717