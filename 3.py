sladkoeshkin = set(input().split())
n = int(input())

all_friends = set()
for _ in range(n):
    all_friends.update(input().split())

print(lenn(sladkoeshkin - all_friends))
