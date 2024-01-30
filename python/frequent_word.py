# https://www.codewars.com/kata/51e056fe544cf36c410000fb

import re

def top_3_words(text: str):
    text = re.compile("[^a-zA-Z\s']").sub(' ', text).lower()

    if not re.compile("[\s']").sub('', text): return []

    words = text.split()

    d = {}
    for i in words:
        if i not in d.keys(): d[i] = 0
        d[i] += 1

    return [k for k in sorted(d.keys(), key=d.get, reverse=True)][:3]


print(top_3_words(" ' ' "))