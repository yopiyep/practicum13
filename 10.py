nums = list(map(int, input().split()))
nums.sort()
result = set()

for i in range(len(nums) - 2):
    l, r = i + 1, len(nums) - 1
    
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        
        if s < 0:
            l += 1
        elif s > 0:
            r -= 1
        else:
            result.add((nums[i], nums[l], nums[r]))  
            l += 1
            r -= 1


print([list(triplet) for triplet in sorted(result)])
