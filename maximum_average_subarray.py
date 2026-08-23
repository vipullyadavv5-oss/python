class Solution(object):
    def findMaxAverage(self, nums, k):
        current = sum(nums[:k])
        best = current

        for i in xrange(k, len(nums)):
            current += nums[i] - nums[i - k]
            best = max(best, current)

        return float(best) / k
