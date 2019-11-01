import os

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for e in vec for num in e])

# 列出当前文件夹下所有的Python源文件
a = [fn for fn in os.listdir('.') if fn.endswith('.py')]
print(a)

# 过滤不符合条件的元素


# 过滤只保留list中的字符串
aList = [-1, -2.3, 'hello', -11, 'xxx']
b = [i for i in aList if type(i) == type('aa')]

# 列表推导式实现矩阵转置


# 元组创建
a = 3,
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(a[0::2]) + list(a[1::2])
print(b)

# 序列解包
v_tuple = (False, 3.5, 'exp')
x, y, z = v_tuple
print(x, y, z)

# 生成器推导式
g = [(i + 2) ** 2 for i in range(10)]
print(g)

# 集合
a = {2, 5}
a.add(7)

a = set([8, 9, 10, 11, 12, 13])
b = set([0, 1, 2, 3, 7, 8])
print(a.union(b))
print(a | b)
print(a.intersection(b))
print(a & b)
print(a.difference(b))
print(a - b)
print(a.symmetric_difference(b))
print(a ^ b)

# 利用集合提取序列中单一元素
# highestPerson = [name for name,scores in scores.items() if scores==highest]
