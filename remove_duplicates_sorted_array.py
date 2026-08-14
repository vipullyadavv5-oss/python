class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        pos = 1

        for i in xrange(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[pos] = nums[i]
                pos += 1

        return pos
