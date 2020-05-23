# 每一趟比较次数的优化
# 总比较趟数的优化

nums = [6, 5, 3, 1, 8, 7, 2, 4]

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print(nums)

# i = 0
# while i < len(nums) - 1:
#     i += 1
#     n = 0
#     while n < len(nums) - 1:
#         if nums[n] > nums[n + 1]:
#             nums[n], nums[n + 1] = nums[n + 1], nums[n]
#         n += 1
# print(nums)
