# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/

import re

def strip_comments(strng: str, markers: list):
    if not markers: return strng
    
    lst = strng.split("\n")

    rgx = re.compile("|".join(f"\{i}" for i in markers))

    for i in range(len(lst)):
        lst[i] = rgx.split(lst[i])[0].strip()

    return "\n".join(lst)

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', []))


# 'apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']), 'apples, pears\ngrapes\nbananas'
# 'a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd'