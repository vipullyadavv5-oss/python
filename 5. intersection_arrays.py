class Solution(object):
    def intersection(self, nums1, nums2):
        first = set(nums1)
        second = set(nums2)

        result = []

        for num in first:
            if num in second:
                result.append(num)

        return result
