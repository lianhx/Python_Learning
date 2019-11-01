# list = [[1, 2, 3, 4],  # 创建一个二维列表
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16],
#         [17, 18, 19, 20]]
# for i in range(5):  # 循环打印数组
#     print(list[i])



# import numpy as np  # 导入numpy模块

# a = np.array(range(1, 5))  # 创建一个一位数组
# b = np.array([a, a+4, a+8, a+12, a+16])  # 创建二维数组
# print(b)  # 打印列表




a = [[1, 2, 3, 4] for i in range(5)]  # 创建5行均为1,2,3,4的二位数组
for i in range(5):
    for j in range(4):
        a[i][j] += i*4
print(a)  # 打印二位数组
