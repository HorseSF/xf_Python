def add_many(iter):
    x = 0
    for n in iter:
        x += n
    return x


nums = [1, 2, 3, 4, 5, 9, 19, 12]
print(add_many(nums))

print(add_many((5, 8, 2, 1, 0, 9, 7, 4)))
