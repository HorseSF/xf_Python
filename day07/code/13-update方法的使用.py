# 列表可以使用extend方法将两个列表合并成一个列表
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9]
nums1.extend(nums2)
print(nums1)
print(nums1 + nums2)

# 字典可以使用update方法将两个字典合并
person1 = {"name": "zhangsan", "age": 18}
person2 = {"addr": "襄阳", "height": 180}
person1.update(person2)
print(person1)
# 字典不支持加法运算

# 两个元组合并为一个元组
words1 = ("hello", "good")
words2 = ("yes", "ok")
print(words1 + words2)