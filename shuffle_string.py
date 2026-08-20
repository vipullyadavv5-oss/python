class Solution(object):
    def restoreString(self, s, indices):
        result = [''] * len(s)

        for i in xrange(len(s)):
            result[indices[i]] = s[i]

        return ''.join(result)
