import random


# 编写一个函数，求多个数中的最大值
def get_max(*args):
    x = args[0]
    for arg in args:
        if arg > x:
            x = arg
    return x


print(get_max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 编写一个函数，实现摇骰子的功能，打印N个骰子的点数和
def get_sum(n):
    m = 0
    i = 1
    for i in range(n):
        x = random.randint(1, 6)
        m += x
    return m


print(get_sum(3))


# 编写一个函数，提取指定字符串中的所用字母，然后拼接在一起产生一个新的字符串
def get_alphs(word):
    new_str = ''
    for w in word:
        if w.isalpha():
            new_str += w
    return new_str


print(get_alphs('123abc456zxc789qwe'))


# 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘
def get_factorial(n=10):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


print(get_factorial())


# 写一个函数，求多个数的平均值
def get_average(*args):
    sum_num = 0
    for arg in args:
        sum_num += arg
    average = sum_num / len(args)
    return average


print(get_average(1, 2, 3, 4, 5, 6))


# 写一个自己的capitalize函数，能够将指定字符串的首字母变成大写字母
def my_capitalize(word):
    c = word[0]
    if c.isalpha():
        new_str = word[1:]
        new_str = c.upper() + new_str
        return new_str
    else:
        return word


print(my_capitalize("c1cc"))


# 写一个自己的endswith函数，判断一个字符串是否以指定的字符串结束
def my_endswith(old_str, check_str):
    return old_str[-len(check_str):] == check_str


print(my_endswith('12345', '45'))


# 写一个自己的isdigit函数，判断一个字符串是否是纯数字字符串
def my_isdigit(str):
    for s in str:
        if not '0' <= s <= '9':
            return False
    return True


print(my_isdigit('1234h56'))


# 写一个自己的upper函数，将一个字符串中所有小写字母变成大写字母
def my_upper(str):
    new_str = ''
    for s in str:
        if 'a' <= s <= 'z':
            new_str += chr(ord(s) - 32)
        else:
            new_str += s
    return new_str


print(my_upper('123aBc456'))


# 写一个函数实现自己in操作，判断指定序列中，指定的元素是否存在
def my_in(it, ele):
    for i in it:
        if i == ele:
            return True
    else:
        return False


print(my_in(['zhangsahn', 'lisi'], 'lisi'))


# 写一个自己的replace函数，将指定字符串中的指定的旧字符串换成指定的新字符串
def my_replace(all_str, old_str, new_str):
    result = ''
    i = 0
    while i < len(all_str):
        temp = all_str[i:i + len(old_str)]
        if temp != old_str:
            result += all_str[i]
            i += 1
        else:
            result += new_str
            i += len(old_str)
    return result


print(my_replace('how you and you fine you ok', 'you', 'me'))


# 写一个自己的max函数，获取指定序列中元素的最大值，如果序列是字典，取字典值得最大值
def get_max2(seq):
    if type(seq) == dict:
        seq = list(seq.values())
    x = seq[0]
    for i in seq:
        if x < i:
            x = i
    return x


print(get_max2([2, 1, 45, 76, 123, 56, 12, 56]))
print(get_max2({'x': 10, 'y': 1, 'z': 12}))
