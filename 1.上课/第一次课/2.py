import math  # 导入math模块

side1 = int(input("请输入一个边长："))  # 得到一个边长
side2 = int(input("请输入另一个边长："))  # 得到第二个边长
angle = int(input("请输入夹角："))  # 得到夹角的值
a = 2*side1*side2*math.cos(angle*math.pi/180)
side3 = math.sqrt(side1**2 + side2**2 - a)  # 利用余弦定理计算第三条边长
print(side3)  # 打印第三条边长
