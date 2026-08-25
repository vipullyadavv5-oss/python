class Solution(object):
    def subsets(self, nums):
        result = [[]]

        for num in nums:
            new_sets = []

            for subset in result:
                new_sets.append(subset + [num])

            result += new_sets

        return result
