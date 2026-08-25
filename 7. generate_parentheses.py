class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def build(current, opening, closing):
            if len(current) == 2 * n:
                result.append(current)
                return

            if opening < n:
                build(current + '(', opening + 1, closing)

            if closing < opening:
                build(current + ')', opening, closing + 1)

        build('', 0, 0)

        return result
