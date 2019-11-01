"""
Python中的集合跟数学上的集合是一致的，不允许有重复元素，
而且可以进行交集、并集、差集等运算。
"""

def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length = ', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)  # 添加元素
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)  # 删除元素
    print(set2)
    if 4 in set2:
        set2.remove(4)  # remove的元素如果不存在会引发KeyError
    print(set2)
    for elem in set2:  # 遍历集合容器
        print(elem ** 2, end=' ')
    print()
    set3 = set((1, 2, 3, 3, 2, 1))  # 将元组转换成集合
    print(set3.pop())
    print(set3)
    print(set1 & set2)  # 交集
    # print(set1.intersection(set2))
    print(set1 | set2)  # 并集
    # print(set1.union(set2))
    print(set1 - set2)  # 差集
    # print(set1.difference(set2))
    print(set1 ^ set2)  # 对称差
    # print(set1.symmetric_difference(set2))
    print(set2 <= set1)  # 判断子集和超集
    print(set2.issubset(set1))


if __name__ == '__main__':
    main()
