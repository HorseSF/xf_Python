def show_menu():
    print("""
    -------------------------
         名片管理系统 V1.0
    1：添加名片
    2：删除名片
    3：修改名片
    4：查询名片
    5：显示所有名片
    6：退出系统
    -------------------------
    """)


def main():
    ctrl = True
    bc_list = []
    while ctrl:
        show_menu()
        option = input("请输入要进行的操作(数字):")
        if option == "1":
            add_bc(bc_list)
        elif option == "2":
            delete_bc(bc_list)
        elif option == "3":
            modify_bc(bc_list)
        elif option == "4":
            search_bc(bc_list)
        elif option == "5":
            show_bc(bc_list)
        elif option == "6":
            esc = input("确定要退出系统吗？Y/N：")
            if esc == "y" or esc == "Y":
                ctrl = False


def add_bc(bc_list):
    name = input("请输入姓名：")

    for i in bc_list:
        if name == i["name"]:
            print("输入的姓名已经存在。")
            break
    else:
        tel = input("请输入电话：")
        qq = input("请输入QQ：")

        bc = {"name": name, "tel": tel, "qq": qq}
        bc_list.append(bc)


def delete_bc(bc_list):
    code = int(input("请输入要删除的序号："))
    bc_list.pop(code)


def modify_bc(bc_list):
    code = int(input("请输入要修改的序号："))
    print("姓名：{}, 电话：{}, QQ：{}".format(bc_list[code]["name"], bc_list[code]["tel"], bc_list[code]["qq"]))
    name = input("请输入新姓名：")
    tel = input("请输入新电话：")
    qq = input("请输入新QQ：")

    bc_list[code]["name"] = name
    bc_list[code]["tel"] = tel
    bc_list[code]["qq"] = qq


def search_bc(bc_list):
    name = input("请输入您要查询的姓名：")

    for i in bc_list:
        if name == i["name"]:
            print("姓名：{}, 电话：{}, QQ：{}".format(i["name"], i["tel"], i["qq"]))
            break
    else:
        print("没有找到要查询的信息...")


def show_bc(bc_list):
    print("序号\t姓名\t电话\tQQ")
    for i, info in enumerate(bc_list):
        print("{}\t{}\t{}\t{}".format(i, info["name"], info["tel"], info["qq"]))


if __name__ == "__main__":
    main()
