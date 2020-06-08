class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # if self.name == other.name and self.age == other.age:
        #     return True
        # return False

        return self.name == other.name and self.age == other.age


p1 = Person("zhangsan", 18)
p2 = Person("zhangsan", 18)

# p1 和 p2不是一个对象，内存空间不同
print("0x%X" % id(p1))
print("0x%X" % id(p2))

# 身份运算符 is 可以判断两个对象是否是同一个对象
# is 比较两个对象的内存地址
# == 调用__eq__方法，获取这个方法的比较结果
# 默认比较内存地址
print(p1 is p2)
print(p1 == p2)

nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print(nums1 is nums2)
print(nums1 == nums2)
