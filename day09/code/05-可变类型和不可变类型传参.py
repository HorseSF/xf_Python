def test(a):
    print("修改前a的内存地址0x%X" % id(a))
    a = 100
    print("修改后a的内存地址0x%X" % id(a))


def demo(nums):
    print("修改后nums的内存地址0x%X" % id(nums))
    nums[0] = 10
    print("修改后nums的内存地址0x%X" % id(nums))


x = 1
test(x)
print(x)

y = [3, 5, 6, 8, 2]
demo(y)
print(y)
