nums = [0, 1, -2, 3, -4, 5, -6, 7, -8, 9]
count = 0

for number in nums:
    if number > 0:
        count += 1
print('number of postives:', count)