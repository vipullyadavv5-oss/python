class Solution(object):
    def stoneGameVIII(self, stones):
        n = len(stones)

        for i in xrange(1, n):
            stones[i] += stones[i - 1]

        best = stones[n - 1]

        for i in xrange(n - 2, 0, -1):
            best = max(best, stones[i] - best)

        return best
