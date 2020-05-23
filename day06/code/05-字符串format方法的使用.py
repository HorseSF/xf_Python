
# {} 一一对应
x = "大家好，我是{},我今年{}岁了".format("张三", 18)
print(x)

# {index}
y = "大家好，我是{1},我今年{0}岁了".format(20, "jerry")
print(y)

# {变量}
z = "大家好，我是{name},我今年{age}岁了,我来自{adr}".format(age=18, name="jack", adr="襄阳")
print(z)

d = ["zhangsan", 18, "上海", 180]
b = "大家好，我是{},我今年{}岁了，我来自{},身高{}cm".format(*d)
print(b)

info = {"name": "lisi", "age": 23, "adr": "背景", "height": 190}
b = "大家好，我是{name},我今年{age}岁了，我来自{adr},身高{height}cm".format(**info)
print(b)

