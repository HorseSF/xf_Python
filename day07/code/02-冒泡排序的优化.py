nums = [6, 5, 3, 1, 8, 7, 2, 4]

count = 0
j = 0
while j < len(nums) - 1:
    j += 1
    i = 0
    flag = True  # 比较趟数优化
    while i < len(nums) - j:  # 比较次数优化
        count += 1
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            flag = False
        i += 1
    if flag:
        break
print(nums)
print("比较了%d次" % count)
