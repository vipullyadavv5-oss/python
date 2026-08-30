class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_pos = 0
        max_pos = 0

        for i in xrange(n):
            if nums[i] < nums[min_pos]:
                min_pos = i

            if nums[i] > nums[max_pos]:
                max_pos = i

        left = min(min_pos, max_pos)
        right = max(min_pos, max_pos)

        # Remove both from the front
        option1 = right + 1

        # Remove both from the back
        option2 = n - left

        # Remove one from each side
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)
