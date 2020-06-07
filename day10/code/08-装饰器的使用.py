def can_play(fn):
    def inner(x, y, *args, **kwargs):
        clock = kwargs.get("clock", 23)
        if clock <= 22:
            fn(x, y)
        else:
            print("太晚了，赶紧睡觉")

    return inner


# 开放封闭原则
@can_play
def play_game(name, game):
    print("{}正在玩{}".format(name, game))


play_game("zhangsan", "王者荣耀", clock=23)
play_game("lis", "王者荣耀")
