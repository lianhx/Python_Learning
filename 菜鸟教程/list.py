classmates = ['Micheal', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])  # -1做索引，获取最后一个元素
print(classmates[-2])  # 获取倒数第二个
classmates.append('Adam')  # 添加一个元素到末尾
print(classmates)
classmates.pop()  # 删除末尾元素
print(classmates)
classmates.pop(1)  # 删除指定位置元素
print(classmates)
classmates[0] = 'Sarah'  # 替换指定位置元素
print(classmates)
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']  # 一个list的元素也可以是另一个list,s可看做一个二维数组
L = []  # 空的list，长度为0
