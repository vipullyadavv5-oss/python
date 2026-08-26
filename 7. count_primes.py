class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = False
        prime[1] = False

        p = 2

        while p * p < n:
            if prime[p]:
                multiple = p * p

                while multiple < n:
                    prime[multiple] = False
                    multiple += p

            p += 1

        return sum(prime)
