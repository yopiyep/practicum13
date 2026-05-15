sladkoeshkin = input().split()
n = int(input())

all_friends = []
for _ in range(n):
    all_friends.extend(input().split())

count = 0
for product in sladkoeshkin:
    if product not in all_friends:
        count += 1

print(count)