# 列表推导式作用是使用简单的语法创建一个列表
nums = [i for i in range(10)]
print(nums)

x = [i for i in range(10) if i % 2 == 0]
print(x)

y = [i for i in range(10) if i % 2]
print(y)

points = [(x, y) for x in range(5, 9) for y in range(10, 20)]
print(points)

# 分组列表里的元素，[1,2,3...100]变成[[1,2,3],[4,5,6]....]
m = [i for i in range(1, 101)]
n = [m[j:j + 3] for j in range(0, 100, 3)]
print(n)
