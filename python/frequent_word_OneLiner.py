top_3_words=lambda t:[w for w, _ in __import__("collections").Counter(__import__("re").findall("'*[a-z][a-z']*",t.lower())).most_common(3)]

print(top_3_words("asd dsa asd"))