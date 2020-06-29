# mode 指的是文件的打开方式
# r：只读模式，打开文件后只能读取，不能写入。如果文件不存在会报错。
# w：写入模式，打开文件后只能写入，不能读取。如果文件存在，会覆盖文件，如果文件不存在，会创建文件
# b：以二进制的形式打开文件
# rb：以二进制读取，wb：以二进制写入
# a：追加模式，会在文本最后追加内容，如果文件不存在会创建文件
# r+：可读写
# w+：可写读

file = open('xxx.txt', 'r')
print(file.read())
file.close()

file = open('xxx.txt', 'w')
file.write('hello')
file.close()

file = open('xxx.txt', 'rb')
print(file.read())
file.close()

file = open('xxx.txt', 'wb')
file.write('大家好'.encode('utf8'))
file.close()
