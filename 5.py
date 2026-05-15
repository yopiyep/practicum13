n = int(input())
primes = set(range(2, n))

for i in range(2, int(n ** 0.5) + 1):
    if i in primes:
        for multiple in range(i * i, n, i):
            primes.discard(multiple)

print(*sorted(primes))