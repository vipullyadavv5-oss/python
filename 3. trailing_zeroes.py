class Solution(object):
    def trailingZeroes(self, n):
        result = 0

        while n > 0:
            n //= 5
            result += n

        return result
