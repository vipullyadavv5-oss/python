class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        result = n

        for i in xrange(n):
            result ^= i
            result ^= nums[i]

        return result
