class Solution(object):
    def lexGreaterPermutation(self, s, target):
        count = [0] * 26

        for ch in s:
            count[ord(ch) - 97] += 1

        n = len(target)
        used = []

        for i in xrange(n):
            x = ord(target[i]) - 97

            # If we cannot use target[i],
            # try a larger character here.
            if count[x] == 0:
                for c in xrange(x + 1, 26):
                    if count[c] > 0:
                        count[c] -= 1

                        ans = target[:i] + chr(c + 97)

                        for j in xrange(26):
                            ans += chr(j + 97) * count[j]

                        return ans

                break

            # Use the same character first
            count[x] -= 1
            used.append(x)

        # We matched the entire target.
        # Now backtrack to make it strictly larger.
        for i in xrange(len(used) - 1, -1, -1):
            count[used[i]] += 1
            x = used[i]

            for c in xrange(x + 1, 26):
                if count[c] > 0:
                    count[c] -= 1

                    ans = target[:i] + chr(c + 97)

                    for j in xrange(26):
                        ans += chr(j + 97) * count[j]

                    return ans

        return ""
