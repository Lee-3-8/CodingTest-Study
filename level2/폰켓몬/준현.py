nums = [3, 3, 3, 2, 2, 2]
arr = []
count = 0
for i in nums:
    if count >= len(nums)//2:
        break
    try:
        arr.index(i)
    except ValueError:
        arr += [i]
        count += 1
print(count)
