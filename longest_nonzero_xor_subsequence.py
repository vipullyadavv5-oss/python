class Solution(object):
    def longestSubsequence(self, nums):
        xor_value = 0

        for num in nums:
            xor_value ^= num

        if xor_value != 0:
            return len(nums)

        # If total XOR is 0, remove one non-zero element.
        for num in nums:
            if num != 0:
                return len(nums) - 1

        return 0
