# 房子（House）有户型，总面积，剩余面积和家具名称列表属性
# 新房子没有人户家具
# 将家具的名称追加到家具名称列表中
# 判断家具的面积是否超过剩余面积，如果超过，提示不能添加这件家具
# 家具（Furniture）有名字和占地面积属性，其中
# 席梦思（bed）占地4平米
# 衣柜（chest）占地2平米
# 餐桌（table）占地1.5平米
# 将以上三件家具添加到房子中
# 打印房子时，要求输出：户型，总面积，剩余面积，家具名称列表


class House(object):
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:
            fru_list = []
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self, x):
        if self.free_area < x.area:
            print('剩余面积不足')
        else:
            self.fru_list.append(x.name)
            self.free_area -= x.area

    def __str__(self):
        return '户型={},总面积={},剩余面积={}，家具列表={}'.format(self.house_type, self.total_area, self.free_area, self.fru_list)


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


house = House('两室一厅', 20)

bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)
sofa = Furniture('沙发', 20)

house.add_fru(bed)
house.add_fru(chest)
house.add_fru(table)
house.add_fru(sofa)

print(house)
