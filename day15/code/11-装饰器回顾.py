def can_play(fn):
    print('外部函数被调用')

    def inner(name, game, **kwargs):
        clock = kwargs.get('clock', 21)
        if clock >= 21:
            print('太晚了')
        else:
            fn(name, game)

    return inner


@can_play
def play_game(name, game):
    print(name + '张在玩' + game)


play_game('张三', '王者荣耀', clock=21)
