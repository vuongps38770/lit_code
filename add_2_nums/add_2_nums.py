class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            su = 0
            while num>0:
                su += num % 10
                num//=10
            num = su
        return num
sol = Solution()
test = 36
print(sol.addDigits(test))