import math


def quadratic(a, b, c):
    m = b**2 - 4 * a * c
    if m >= 0:
        x1 = (-b + math.sqrt(m)) / (2 * a)
        x2 = (-b - math.sqrt(m)) / (2 * a)
        return x1, x2
    else:
        print('方程没有实根')


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
