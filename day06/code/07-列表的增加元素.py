# 列表的增删改查

heros = ["阿珂", "嬴政", "韩信", "露娜","后裔" "李元芳"]

# 添加元素的方法 append insert extend
# 列表的最后面添加
heros.append("黄忠")
print(heros)

# 指定index位置插入
heros.insert(3, "李白")
print(heros)

# 拼接
x = ["马可波罗", "米莱迪", "狄仁杰"]
heros.extend(x)
print(heros)

