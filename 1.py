nums = map(int, input().split())
target = int(input())
ver = 0

for num in nums:
    if num == target:
        ver += 1

if ver > 0:
    print('True')
else:
    print('False')