from typing import List

def subsetXORSum(nums: List[int]) -> int:
        subSets = [[]]

        for i in nums:
            subSets += [item + [i] for item in subSets]

        print(*subSets, sep="\n")

        sum = 0

        for subSet in subSets:
            if not len(subSet):
                continue
            
            if len(subSet) == 1:
                sum += subSet[0]
                continue
            
            b = 0
            for i in range(len(subSet)):
                b = b ^ subSet[i]
                
            sum+=b
        
        print(sum)
                    


            

subsetXORSum([5, 1, 6]) # 28

# None      -> 000      0
# 5         -> 101      5
# 1         -> 001      1
# 6         -> 110      6
# 5,1       -> 101
#              001
#              100      4
# 5,6       -> 101
#              110
#              011      3
# 1,6       -> 001
#              110
#              111      7
# 5,1,6     -> 101
#              001
#              100
#              110
#              010      2