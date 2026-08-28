class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        count = [0] * 26

        for ch in s:
            count[ord(ch) - 97] += 1

        # A palindrome can have at most one odd frequency
        odd = []

        for i in xrange(26):
            if count[i] % 2:
                odd.append(i)

        if len(odd) > 1:
            return ""

        middle = ""
        if odd:
            middle = chr(odd[0] + 97)

        # Construct the multiset for the left half
        half = []

        for i in xrange(26):
            half += [chr(i + 97)] * (count[i] // 2)

        m = len(half)

        best = None

        # Case 1:
        # The left half is exactly target[:m].
        # The resulting complete palindrome may still be > target.
        available = [0] * 26

        for ch in half:
            available[ord(ch) - 97] += 1

        possible = True

        for i in xrange(m):
            x = ord(target[i]) - 97

            if available[x] == 0:
                possible = False
                break

            available[x] -= 1

        if possible:
            left = target[:m]
            candidate = left + middle + left[::-1]

            if candidate > target:
                best = candidate

        # Case 2:
        # Find the smallest left half strictly greater
        # than target[:m].
        #
        # Try every possible position where the first
        # greater character occurs.
        for pos in xrange(m - 1, -1, -1):

            available = [0] * 26

            for ch in half:
                available[ord(ch) - 97] += 1

            possible = True

            # Match target prefix before pos
            for j in xrange(pos):
                x = ord(target[j]) - 97

                if available[x] == 0:
                    possible = False
                    break

                available[x] -= 1

            if not possible:
                continue

            x = ord(target[pos]) - 97

            # Choose the smallest possible character
            # greater than target[pos]
            for c in xrange(x + 1, 26):

                if available[c] == 0:
                    continue

                available[c] -= 1

                left = target[:pos]
                left += chr(c + 97)

                # Fill remaining positions in sorted order
                for j in xrange(26):
                    left += chr(j + 97) * available[j]

                candidate = left + middle + left[::-1]

                if candidate > target:
                    if best is None or candidate < best:
                        best = candidate

                available[c] += 1

        if best is None:
            return ""

        return best
