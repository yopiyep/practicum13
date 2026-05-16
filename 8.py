from itertools import combinations


elements = sorted(set(input().split()))
subsets = []

for r in range(len(elements) + 1):           # внешний цикл по размерам
    for comb in combinations(elements, r):   # внутренний цикл по комбинациям
        subsets.append(list(comb))

for subset in subsets:
    print(' '.join(subset))
