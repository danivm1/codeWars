# https://www.codewars.com/kata/52996b5c99fdcb5f20000004

def runoff(voters: list[list]):
    while True:
        for x, i in enumerate(voters):
            for j in i[::-1]:
                if j not in [v[0] for v in voters]:
                    voters[x].remove(j)
        
        if not i: return None

        candidates = voters[0]
        d = {k: 0 for k in candidates}


        for i in [i[0] for i in voters]:
            d[i] += 1

        ma = max(d.values())

        if ma > sum(d.values()) // 2:
            return max(d, key=d.get)

        mi = min(d.values())
        lessers = [k for k, v in d.items() if v == mi]

        for x, i in enumerate(voters):
            voters[x] = [i for i in voters[x] if i not in lessers]

    
        


# [["d", "b"],
#  ["d", "b"],
#  ["d", "b"],
#  ["d", "b"],
#  ["b", "d"],
#  ["b", "d"],
#  ["b", "d"]]

# {"a": 1,
#  "b": 3,
#  "d": 3}        

voters = [["a", "c", "d", "e", "b"],
                 ["e", "b", "d", "c", "a"],
                 ["d", "e", "c", "a", "b"],
                 ["c", "e", "d", "b", "a"],
                 ["b", "e", "a", "c", "d"]]

print(runoff(voters))