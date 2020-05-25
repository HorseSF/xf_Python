import copy

# 浅复制
nums1 = [1, 2, 3, 4, 5]

nums2 = nums1.copy()

nums3 = copy.copy(nums1)

# 深复制，只能用copy模块实现
words = ["hello", "good", [100, 200, 300], "yes", "hi", "ok"]

# words1是words的浅复制
# 只复制了一层
words1 = words.copy()

# words2是words的深复制
words2 = copy.deepcopy(words)

words[2][0] = 1
print(words1)

words[2][1] = 2
print(words2)
