word = input("请输入三个字母(以空格间隔)：")  # 输入数据
x, y, z = word.split()  # 对字符串进行切片
if x > y:  # 进行排序
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)  # 打印排序后的字母
