# 集合是一个不重复的无序集合，可以使用{} 或set来表示
# {}有两种意思：字典，集合

person = {"name": "zhangsan"}
x = {"hello", 1, "good"}

# 如果有重复数据会自动去重
names = {"zhangsan", "lisi", "jack", "tony", "zhangsan"}
print(names)

names.add("阿珂")  # 添加一个元素
print(names)

names.pop()  # 随机删除一个元素
print(names)

names.remove("jack")  # 删除指定元素
print(names)

print(names.union({"刘能", "赵四"}))  # 求并集,返回新集合

names.update({"刘能", "赵四"})  # 求并集，返回到原有集合
print(names)

names.clear()  # 清空一个集合
print(names)  # {}表示空字典 set()表示空集合
