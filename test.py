nums = [5,5,1,1,1,5,5]
occurrence = {}

for num in nums:
    occurrence[num] = 1 + occurrence.get(num, 0)

max_num = max(occurrence, key=occurrence.get)

print(occurrence)
print(max_num)