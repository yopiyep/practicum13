from itertools import combinations


elements = sorted(set(input().split()))
subsets = []

for r in range(len(elements) + 1):          
    for comb in combinations(elements, r):   
        subsets.append(list(comb))

for subset in subsets:
    print(' '.join(subset))
