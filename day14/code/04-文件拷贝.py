import os

file_name = input('请输入一个文件路径：')  # sss.txt ==> sss.bak.txt

if os.path.isfile(file_name):
    # 打开旧文件
    old_file = open(file_name, 'rb')

    # names = file_name.rpartition('.')
    # new_file_name = names[0] + '.bak.' + names[2]

    names = os.path.splitext(file_name)
    new_file_name = names[0] + '.bak' + names[1]
    new_file = open(new_file_name, 'wb')

    while True:
        content = old_file.read(1024)
        # 把旧文件的数据读取出来写入新文件
        new_file.write(content)
        if not content:
            break

    new_file.close()
    old_file.close()
else:
    print('输入的文件不存在')
