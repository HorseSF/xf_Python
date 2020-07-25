user_permission = 15

# 权限因子
DEL_PERMISSION = 8  # 0b1000
READ_PERMISSION = 4  # 0b0100
WRITE_PERMISSION = 2  # 0b0010
EXE_PERMISSION = 1  # 0b0001


def check_permission(x, y):
    def handle_action(fn):
        def do_action():
            # 用户权限和权限因子按位与运算
            if x & y != 0:
                fn()
            else:
                print('没有权限')

        return do_action

    return handle_action


@check_permission(user_permission, READ_PERMISSION)
def read():
    print('我正在读取内容')


@check_permission(user_permission, WRITE_PERMISSION)
def write():
    print('我正在写入内容')


@check_permission(user_permission, EXE_PERMISSION)
def execute():
    print('我正在执行内容')


@check_permission(user_permission, EXE_PERMISSION)
def delete():
    print('我正在删除内容')


read()
write()
execute()
delete()
