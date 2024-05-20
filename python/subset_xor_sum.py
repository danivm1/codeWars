from typing import List

def subsetXORSum(nums: List[int]) -> int:
        subSets = [[]]

        for i in nums:
            subSets += [item + [i] for item in subSets]

        print(*subSets, sep="\n")

        for subSet in subSets:
            if len(subSet) == 0:
                continue
            if len(subset) == 1:
                
            for i in subSet:
                 

subsetXORSum([5, 1, 6])

# 101 - 5
# 001 - 1
# 100 - 8
# 110 - 6
# 010 - 2