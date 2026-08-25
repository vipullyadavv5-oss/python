class Solution(object):
    def permute(self, nums):
        result = []

        def build(path, remaining):
            if not remaining:
                result.append(path[:])
                return

            for i in xrange(len(remaining)):
                path.append(remaining[i])
                build(path, remaining[:i] + remaining[i + 1:])
                path.pop()

        build([], nums)

        return result
