x = int(input("请输入一个数:\n"))
a = x // 10000
b = x // 1000 % 10
c = x // 100 % 10
d = x // 10 % 10
e = x % 10

if a != 0:
    print("5 位数：", e, d, c, b, a)
elif b != 0:
    print("4 位数：", e, d, c, b)
elif c != 0:
    print("3 位数：", e, d, c)
elif d != 0:
    print("2 位数：", e, d)
else:
    print("1 位数：", e)
