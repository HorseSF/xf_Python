print(bool(100))
print(bool(0))
print(bool('False'))

print(bool(-1))
print(bool(''))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))

# 在计算机里，True和False其实就是使用数字1和0来保存的
print(True + 1)
print(False + 1)

# 隐式类型转换
if 3:
    print('hello')
