nums = [3, 1, 9, 8, 4, 2, 0, 7, 5]
# nums.sort()
# print(nums[-1])

# nums.sort(reverse=True)
# print(nums[0])

maxNum = nums[0]
index = 0
for num in nums:
    if maxNum < num:
        index = nums.index(num)
        maxNum = num
print(maxNum)
print(nums.index(maxNum))
print(index)
