class Solution(object):
    def totalNumbers(self, digits):
        count = [0] * 10

        for d in digits:
            count[d] += 1

        ans = 0

        for a in range(1, 10):
            for b in range(10):
                for c in (0, 2, 4, 6, 8):

                    need = [0] * 10
                    need[a] += 1
                    need[b] += 1
                    need[c] += 1

                    possible = True

                    for d in range(10):
                        if need[d] > count[d]:
                            possible = False
                            break

                    if possible:
                        ans += 1

        return ans
