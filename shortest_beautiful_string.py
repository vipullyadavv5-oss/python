class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ones = []
        n = len(s)

        for i in xrange(n):
            if s[i] == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        best = None
        best_len = n + 1

        for i in xrange(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            length = end - start + 1
            candidate = s[start:end + 1]

            if length < best_len:
                best_len = length
                best = candidate
            elif length == best_len and candidate < best:
                best = candidate

        return best
