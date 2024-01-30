def bucket_sort(lst, qnt):
    b = ((max(lst) + 1) // qnt) + 1 if (max(lst) + 1) % qnt else ((max(lst) + 1) // qnt) 
    bLst = [[] for _ in range(qnt)]

    for i in lst: 
        j = i // b
        bLst[j].append(i)

    lst = []   

    for i in bLst:
        for j in sorted(i):
            lst.append(j)

    return lst

lst = [234, 54, 3, 5, 763, 243, 999]
qnt = 9
print(f"Execução: {__import__('timeit').timeit(lambda: print(bucket_sort(lst, qnt)), number=1)} segundos")



# qtn=9 max=999
# ceil((max+1)/(qnt)) = 112
#  0 0
#  1 112
#  2 224
#  3 336
#  4 448
#  5 560
#  6 672
#  7 784
#  8 896
#  9 1008