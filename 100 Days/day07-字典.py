def main():
    scores = {'李元芳': 95, '狄仁杰': 78, '蓝猫': 82}
    print(scores['李元芳'])  # 通过键可以获取字典中对应的值
    for elem in scores:  # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
        print('%s\t---->\t%d' % (elem, scores[elem]))
    scores['狄仁杰'] = 65  # 更新字典中的元素
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))  # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.popitem())  # 删除字典中的元素
    print(scores.popitem())
    print(scores.pop('李元芳', 95))
    scores.clear()  # 清空字典
    print(scores)


if __name__ == '__main__':
    main()
