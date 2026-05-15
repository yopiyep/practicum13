from itertools import combinations


numbers = sorted(set(input().split()))
K = int(input())

for comb in combinations(numbers, K):
    print(' '.join(comb))