nums = [1,1,2,3,4]
val = 1
res = []

for num in nums:
    if num == val:
        continue
    else:
        res.append(num)
print(res)