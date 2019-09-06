"""
输入一个正整数判断它是不是素数

素数(质数)：指整数在一个大于1的自然数中，除了1和此整数自身外，没法被其他自然数整除的数。
"""
from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
