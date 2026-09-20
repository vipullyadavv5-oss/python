class Solution(object):
    def reverseDegree(self, s):
        total = 0

        for i in xrange(len(s)):
            value = ord(s[i]) - ord('a')
            reverse_value = 26 - value
            position = i + 1

            total += reverse_value * position

        return total
