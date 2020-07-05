import sys

# sys.stdin  # 接收键盘里输入的数据
# sys.stdout  # 标准输出
# sys.stderr  # 错误输出

s_in = sys.stdin

# while True:
#     content = s_in.readline().rstrip('\n')
#     if content == '':
#         break
#     print(content)

sys.stdout = open('stdout.txt', 'w', encoding='utf8')
print('hello')

sys.stderr = open('stderr.txt', 'w', encoding='utf8')
print(1 / 0)
