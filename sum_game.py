class Solution(object):
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in xrange(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in xrange(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Difference in number of '?' must be even
        # because Alice and Bob take turns.
        if (left_q + right_q) % 2 == 1:
            return True

        # Current difference between the two halves.
        diff = left_sum - right_sum

        # If left has more '?' positions
        if left_q > right_q:
            diff += 9 * ((left_q - right_q) // 2)
        else:
            diff -= 9 * ((right_q - left_q) // 2)

        return diff != 0
