class Solution(object):
    def findDifference(self, nums1, nums2):
        a = set(nums1)
        b = set(nums2)

        return [list(a - b), list(b - a)]
