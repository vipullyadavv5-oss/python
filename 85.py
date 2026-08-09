class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)

        # Suffix sum
        suffix = [0] * (n + 1)

        for i in xrange(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dfs(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            for X in xrange(1, 2 * M + 1):
                if i + X <= n:
                    # Current player gets all remaining stones
                    # minus what the opponent can get.
                    opponent = dfs(i + X, max(M, X))
                    best = max(best, suffix[i] - opponent)

            memo[(i, M)] = best
            return best

        return dfs(0, 1)
