class Solution(object):
    def missingMultiple(self, nums, k):
        values = set(nums)
        multiple = k

        while multiple in values:
            multiple += k

        return multiple
