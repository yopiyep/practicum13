from itertools import combinations


elements = sorted(set(input().split()))
subsets = [list(comb) for r in range(len(elements) + 1) for comb in combinations(elements, r)]

for subset in subsets:
    print(' '.join(subset))