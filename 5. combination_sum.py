class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def search(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in xrange(start, len(candidates)):
                if candidates[i] > remaining:
                    continue

                path.append(candidates[i])
                search(i, remaining - candidates[i], path)
                path.pop()

        candidates.sort()
        search(0, target, [])

        return result
