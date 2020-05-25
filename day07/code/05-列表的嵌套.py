import random

# 多维数组
nums = [1, 2, [100, 200, 500], 3, 4, 5]

# 一个学校有3个办公室，现在有8位老师等待分配工位，请完成随机的分配
teachers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
rooms = [[], [], []]

for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)

# 第0个房间有几个人，分别是谁
for i, room in enumerate(rooms):
    print("房间%d里有%d个老师" % (i, len(room)))
    for teacher in room:
        print(teacher)
