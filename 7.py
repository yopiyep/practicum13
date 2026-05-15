from itertools import permutations


numbers = input().split()

unique_numbers = sorted(set(numbers))
for perm in permutations(unique_numbers):
    print(' '.join(perm))