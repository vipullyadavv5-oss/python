class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        used = set()

        for ch, word in zip(pattern, words):
            if ch in mapping:
                if mapping[ch] != word:
                    return False
            else:
                if word in used:
                    return False

                mapping[ch] = word
                used.add(word)

        return True
