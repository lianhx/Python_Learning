def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    print(len(list1))  # 计算列表长度(元素个数)
    print(list1[0])  # 下标(索引)运算
    print(list1[4])
    print(list1[-1])
    print(list1[-3])
    list1.append(200)  # 添加元素
    list1.insert(1, 400)  # 在1位置插入一个元素
    list1 += [1000, 2000]
    print(list1)
    print(len(list1))
    list1.remove(3)  # 删除元素3这个数
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]
    print(list1)
    list1.clear()  # 清空列表元素
    print(list1)


if __name__ == '__main__':
    main()
