age = input('请输入年龄：')

# if age.isdigit():
try:
    age = int(age)
except ValueError as e:
    print('输入的不是数字')
else:
    if age > 18:
        print('欢迎来到我的网站')
    else:
        print('请离开')
