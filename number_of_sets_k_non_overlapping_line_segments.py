class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 1000000007

        a = n + k - 1
        b = 2 * k

        numerator = 1
        denominator = 1

        for i in xrange(1, b + 1):
            numerator = numerator * (a - i + 1) % MOD
            denominator = denominator * i % MOD

        return numerator * pow(denominator, MOD - 2, MOD) % MOD
