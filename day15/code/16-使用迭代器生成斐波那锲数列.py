class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.n:
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


# 1,1,2,3,5,8,13,21,34,55,89,144
f = Fibonacci(12)
for i in f:
    print(i)

# 为什么要有迭代器
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 占空间，不占时间
nums2 = range(1, 10)  # 占时间，不占空间
