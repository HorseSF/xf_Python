import csv

file = open('demo.csv', 'w')
w = csv.writer(file)
# w.writerow(['name', 'age', 'score', 'city'])
#
# w.writerow(['张三', '19', '90', '襄阳'])
# w.writerow(['李四', '19', '80', '纽约'])

w.writerows(
    [
        ['name', 'age', 'score', 'city'],
        ['张三', '19', '90', '襄阳'],
        ['李四', '19', '80', '纽约']
    ]
)
file.close()

file = open('info.csv', 'r')
r = csv.reader(file)
for data in r:
    print(data)

file.close()
