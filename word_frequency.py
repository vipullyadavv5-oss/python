"""Word Frequency Counter

Count how many times each word appears in a text block.
"""

import re
from collections import Counter


def word_frequency(text):
    cleaned_text = re.findall(r"\b\w+\b", text.lower())
    return Counter(cleaned_text)


if __name__ == "__main__":
    sample = """
    Python is fun and easy to learn. Python helps build applications,
    scripts, and automation. Learning Python is useful for beginners and experts.
    """
    result = word_frequency(sample)
    for word, count in result.most_common():
        print(f"{word}: {count}")
