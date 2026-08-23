class Solution(object):
    def findWords(self, words):
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []

        for word in words:
            letters = set(word.lower())

            for row in rows:
                if letters <= row:
                    result.append(word)
                    break

        return result
