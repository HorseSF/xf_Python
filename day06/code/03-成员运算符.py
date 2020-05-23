# in not in
# 用来判断一个内容在可迭代对象里是否存在

word = "hello"
x = input("请输入一个字符：")

# 判断用户输入的内容是否存在
# for i in word:
#     if x == i:
#         print("存在")
#         break
# else:
#     print("不存在")

# if word.find(x) == -1:
#     print("不存在")
# else:
#     print("存在")

if x in word:
    print("存在")
else:
    print("不存在")
