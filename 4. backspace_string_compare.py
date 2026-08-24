class Solution(object):
    def backspaceCompare(self, s, t):
        def build(text):
            stack = []

            for ch in text:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)

            return ''.join(stack)

        return build(s) == build(t)
