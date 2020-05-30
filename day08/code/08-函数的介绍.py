# 函数就是一堆准备好的代码，在需要的时候调用
# def 函数名(参数):
#   函数要执行的操作

def tell_story():
    print("从前有座山")
    print("山上有座庙")
    print("庙里有个老和尚")
    print("还有一个小和尚")
    print("老和尚在给小和尚讲故事")
    print("故事的内容是")


age = int(input("请输入孩子的年龄："))
if 0 <= age <= 3:
    for _ in range(5):
        tell_story()
elif 5 > age > 3:
    for _ in range(3):
        tell_story()
else:
    tell_story()
