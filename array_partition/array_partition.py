class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[0::2])
    
# test
sol = Solution()
test = [1,3,5,2]
print(sol.arrayPairSum(test))