person = {"name": "zhangsan",
          "age": 18,
          "height": 180,
          "isPass": True,
          "hobbies": ["唱", "跳", "篮球", "Rap"],
          4: "good",
          ("yes", "hello"): 100
          }

print(person)

# 字典里的key不能重复，如果重复了，后一个key对应的值会覆盖前一个
# 字典里的value可以是任意数据类型，但是key只能使用不可变数据类型，一般使用字符串
