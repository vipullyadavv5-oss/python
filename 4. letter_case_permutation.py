class Solution(object):
    def letterCasePermutation(self, s):
        result = ['']

        for ch in s:
            current = []

            if ch.isalpha():
                for item in result:
                    current.append(item + ch.lower())
                    current.append(item + ch.upper())
            else:
                for item in result:
                    current.append(item + ch)

            result = current

        return result
