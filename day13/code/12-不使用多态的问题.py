class PoliceDog(object):
    def attack_enemy(self):
        print('警犬正在攻击坏人')


class BlindDog(object):
    def lead_road(self):
        print('导盲犬正在领路')


class Person(object):
    def __init__(self, name):
        self.name = name

    def work_with_pd(self):
        print(self.name + '正在工作')
        self.dog.attack_enemy()

    def work_with_bd(self):
        self.dog.lead_road()


p = Person('张三')

pd = PoliceDog()
p.dog = pd
p.work_with_pd()

bd = BlindDog()
p.dog = bd
p.work_with_bd()
