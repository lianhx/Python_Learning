def main():
    t = ('连海旭', 20, True, '四川成都')  # 定义元组
    print(t)
    print(t[0])  # 获取元组中的元素
    print(t[3])
    for member in t:  # 遍历元组的值
        print(member)
    # t[0] = '王大锤'  # TypeError 元组不可更改元素
    t = ('王大锤', 30, True, '云南昆明')  # 重新给元组赋值
    print(t)
    person = list(t)  # 将元组转换成列表
    print(person)
    person[0] = '李小龙'  # 列表是可以修改元素的
    person[1] = 25
    print(person)
    fruit_list = ['apple', 'banana', 'orange']
    fruit_tuple = tuple(fruit_list)  # 将列表转换成元组
    print(fruit_tuple)


if __name__ == '__main__':
    main()
